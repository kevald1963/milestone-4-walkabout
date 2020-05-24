import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.template import RequestContext
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from organisation.forms import EditOrganisationForm
from organisation.models import Organisation
from product.models import Product
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem, Order

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
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            if total > 0 and payment_form.is_valid():
                # ========================================================================================
                # Only make payments where a cost is incurred and valid payment details have been entered
                # i.e. skip for free base product.
                # ========================================================================================
                try:
                    customer = stripe.Charge.create(
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
                if total > 0:
                    print(payment_form.errors)
                    messages.error(request, "We were unable to take a payment with that card!")

            # =============================================================================================
            # If payment has been taken or the product is free, then check if organisation exists for this
            # signed-in user. If it doesn't, then create it from the supplied order details.
            # =============================================================================================
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
            existing_admin_group = Group.objects.get(name='Administrator')
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
                # If the Administrator group does not exist, then create and save it before adding user to it.
                # ============================================================================================
                new_group = Group(name='Administrator')
                new_group.save()
                # Get the current user and add to newly created group.
                this_user = User.objects.get(username=request.user)
                this_user.group.add(new_group)

            if total > 0:
                messages.error(request, "You have been successfully subscribed to our FREE product.")
            else:
                messages.error(request, "You have successfully paid.")

            # Empty the Cart now that the subscription has been successfully taken out.
            request.session['cart'] = {}
            return redirect(reverse('all_products'))
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html",
                  {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})


def save_details(request):
    if request.method == "POST":
        """ Process form -  still to do."""
    else:
        form = EditOrganisationForm()
        # Get the order belonging to this user.
        form.fields["order_details"].queryset = Order.objects.filter(user=request.user)

    template_vars = RequestContext(request, {"form": form, "user": request.user})
    return render(request, "process_order.html", template_vars)
