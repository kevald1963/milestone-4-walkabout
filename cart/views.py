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
    print("cart = " + str(cart))
    quantity = int(request.POST.get('quantity[]'))
    print("quantity 1 = " + str(quantity))
    message = ''

    # Check if Free subscription product already saved to database, as it can only be registered once per customer.
    # If it is, then don't add product to Cart.
    if product.is_subscription_product and product.price == 0:
        subscription = Subscription.objects.all().filter(product_number=product.number)
        # If customer already has this product then don't add it to Cart.
        if subscription:
            # do nothing
            print("subscription = " + str(subscription))
            quantity = 0
            messages.add_message(request, messages.INFO, 'Product not added to cart - you own this product already!')
        else:
            quantity = 1

    print("quantity 2 = " + str(quantity))

    # If product is already in cart, update the quantity, otherwise add the product to the
    # cart with the selected quantity.
    if id in cart:
        cart[id] = int(cart[id]) + quantity
        messages.add_message(request, messages.INFO, 'Quantity for this product updated in cart.')
    else:
        cart[id] = cart.get(id, quantity)
        messages.add_message(request, messages.INFO, 'Product added to cart.')

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
