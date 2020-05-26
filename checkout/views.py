import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from organisation.models import Organisation
from product.models import Product
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem

stripe.api_key = settings.STRIPE_SECRET


# Create your views here.
@login_required()
def checkout(request):
    """
    Present payment form for user to enter. Make payments if form is valid and
    update the subscription table with latest purchases.
    NOTE that payment details are not requested from user if subscribing to the
    free product only. Likewise payment processing is bypassed in this view if
    the total product value is zero.
    """
    total = 0
    print("*********** tot 1")
    print(total)
    print("***********")

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            # total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            if total > 0:
                # ========================================================================================
                # Only take payment where a cost is incurred and valid payment details have been entered
                # i.e. skip for free base product.
                # ========================================================================================
                if payment_form.is_valid():
                    try:
                        stripe.Charge.create(
                            amount=int(total * 100),
                            currency="GBP",
                            description=request.user.email,
                            card=payment_form.cleaned_data['stripe_id'],
                        )
                    except stripe.error.CardError:
                        messages.error(request, "Your card was declined!")
                    except Exception:
                        messages.error(request, "An error occurred, couldn't process your request.")
                else:
                    print(payment_form.errors)
                    messages.error(request, "We were unable to take a payment with that card!")

            # =============================================================================================
            # If payment has been taken or the product is free, then check if organisation exists for this
            # signed-in user. If it doesn't, then create it from the supplied order details.
            # =============================================================================================
            print("Got here - even if payment failed!")
            try:
                organisation = Organisation.objects.get(is_parent=True)
            except ObjectDoesNotExist:
                organisation = None

            if not organisation:
                # No parent organisation found, so create it from Order details.
                org = Organisation()
                org.name = order.name
                org.is_parent = True
                org.address_1 = order.address_1
                org.address_2 = order.address_2
                org.address_3 = order.address_3
                org.town_or_city = order.town_or_city
                org.post_code = order.post_code
                org.email_address = order.email_address
                org.mobile_number = order.mobile_number
                org.save()

            # =================================================================================================
            # Update the signed-in user's details, in order to upgrade them to Administrator status, but only
            # if this is their first order on the system. If they have subscribed before they should already
            # have that status. Initial Administrator status is conferred as a result of a first purchase of a
            # base product. Administrator status is set by adding the user to the 'Administrator' group.
            # =================================================================================================
            existing_admin_group = Group.objects.get(name='Administrator2')
            if existing_admin_group:
                # ===========================================================================================
                # If Administrator group exists on Group table then check for any groups the user belongs to.
                # Only add user to the Administrator group if they don't belong to any group whatsoever, as
                # it's undesirable to upgrade a user, initially set as an Agent, to an Administrator, as it
                # may cause security problems. An existing Administrators can upgrade the user manually, if
                # they wish.
                # ===========================================================================================
                user_group = Group.objects.filter(user=request.user).values_list('name', flat=True)
                if not user_group:
                    # If user not in any group then add them to the Administrator group.
                    this_user = User.objects.get(username=request.user)
                    this_user.groups.add(existing_admin_group)
            else:
                # ============================================================================================
                # The Administrator group does not exist, so create it, and save it and add relevant
                # permissions to it before adding the signed-in user to it.
                # ============================================================================================
                content_type = ContentType.objects.get_for_model(User)
                add_user = Permission.objects.get(content_type=content_type, codename='add_user')
                change_user = Permission.objects.get(content_type=content_type, codename='change_user')
                delete_user = Permission.objects.get(content_type=content_type, codename='delete_user')

                new_group, created = Group.objects.get_or_create(name='Administrator2')
                if created:
                    # Assign permissions to newly-created group.
                    new_group.permissions.add(add_user, change_user, delete_user)

                    # Get the current user and add to newly created group.
                    this_user = User.objects.get(username=request.user)
                    this_user.group.add(new_group)

            if total == 0:
                messages.error(request, "You have been successfully subscribed to our FREE product.")
            else:
                messages.error(request, "You have successfully paid.")

            # Empty the Cart now that the subscription has been successfully taken out.
            request.session['cart'] = {}
            return redirect(reverse('all_products'))
        else:
            print(order_form.errors)
            messages.error(request, "Sorry, there is an unexpected technical problem with your order. "
                                    "Please contact us on 0000 1234567 so we can take your order manually.")
    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()

    print("*********** tot 2")
    print(total)
    print("***********")

    return render(request, 'checkout.html', {'order_form': order_form, 'payment_form': payment_form,
                                             'publishable': settings.STRIPE_PUBLISHABLE})
