from django.shortcuts import render, redirect, reverse
from product.models import Product
from organisation.models import Subscription
from django.contrib import messages


# Create your views here.
def view_cart(request):
    """
    A view that renders the cart contents page.
    """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """
    Add a quantity of the specified product to the cart.
    """
    product = Product.objects.get(id=id)

    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity[]'))
    max_product_quantity = int(product.max_product_quantity)

    # Check if product with a single item quantity is already saved to database, as it can only be saved once
    # per parent organisation account. If it is, then do not add product to Cart.
    if max_product_quantity == 1:
        subscription = Subscription.objects.all().filter(product_number=product.number)
        # If customer already has this product then do not add it to Cart.
        if subscription:
            quantity = 0
            messages.add_message(request, messages.INFO,
                                 'Product not added to Cart. This subscription is on your account already!')

    # If product is already in cart, update the quantity, else add the product to the cart with the
    # selected quantity.
    if id in cart:
        # If a single item product with the same id already exists in the cart then do not add it again.
        if max_product_quantity == 1 and int(product.id) == int(id):
            messages.add_message(request, messages.INFO, 'Product is already in Cart. Only one item of '
                                                         'this product is allowed!')
        else:
            cart[id] = int(cart[id]) + quantity
    else:
        if quantity != 0:
            cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('all_products'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified amount.
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def empty_cart(request):
    """
    Clear the Cart of all products.
    """
    cart = request.session.get('cart', {})
    cart.clear()

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
