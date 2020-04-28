import stripe
from django.conf import settings
from django.contrib import messages
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
    """

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
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

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            else:
                if customer.paid:
                    try:
                        # Check if organisation exists for this user.
                        organisation = \
                            Organisation.objects.select_related('user').get(user__is_superuser=True, is_parent=True)
                    except ObjectDoesNotExist:
                        organisation = None

                    if not organisation:
                        print('order_form = ' + str(order))
                        org = Organisation()
                        # If no organisation found, then create it from Order details.
                        org.name = order.name
                        org.address_1 = order.address_1
                        org.address_2 = order.address_2
                        org.address_3 = order.address_3
                        org.town_or_city = order.town_or_city
                        org.post_code = order.post_code
                        org.email_address = order.email_address
                        org.mobile_number = order.mobile_number
                        org.user = request.user
                        org.save()
                    else:
                        print('organisation found!')

                    messages.error(request, "You have successfully paid.")
                    request.session['cart'] = {}
                    return redirect(reverse('all_products'))
                else:
                    messages.error(request, "Unable to take payment.")
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
