from django.shortcuts import get_object_or_404
from product.models import Product


def cart_contents(request):
    """
    Ensure contents are available when rendering every page.
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        # If quantity is zero, do not put the product in the Cart.
        if quantity > 0:
            total += quantity * product.price
            product_count += quantity
            cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}