from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from product.models import Product, Discount
from decimal import *


def cart_contents(request):
    """
    Ensure contents are available when rendering every page.
    """
    cart_items = []
    subtotal = Decimal(0)
    discount_applicable = False
    product_count = 0

    cart = request.session.get('cart', {})
    try:
        percent = Discount.objects.values_list('percent', flat=True).get(code=1)
    except ObjectDoesNotExist:
        messages.error(request, "Error: Discount rate not found. Complementary 12.50% discount applied.")
        percent = 12.5

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)

        # If quantity is zero, do not put the product in the Cart.
        if quantity > 0:
            subtotal += quantity * product.price
            product_count += quantity
            cart_items.append({'id': id, 'quantity': quantity, 'product': product})
            if quantity > 1:
                discount_applicable = True

    if discount_applicable:
        discount_amount = round(subtotal * (percent/100), 2)
    else:
        discount_amount = round(0, 2)

    total = Decimal(subtotal - discount_amount)

    return {'cart_items': cart_items, 'subtotal': subtotal, 'total': total, 'product_count': product_count,
            'percent': percent, 'discount_amount': discount_amount}
