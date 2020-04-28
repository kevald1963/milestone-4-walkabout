from django.shortcuts import render, redirect, reverse
from product.models import Product
from organisation.models import Subscription
from django.contrib import messages


# Create your views here.
def empty_cart(request):
    """
    Clear the Cart of all products.
    """
    cart = request.session.get('cart', {})
    cart.clear()

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def view_cart(request):
    """
    A view that renders the cart contents page.
    """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """
    Add a quantity of the specified product to the cart depending on product type.
    """
    product = Product.objects.get(id=id)

    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity[]'))
    max_product_quantity = int(product.max_product_quantity)
    is_base_product = product.is_base_product

    if max_product_quantity == 1:
        # Check if product with a single item quantity is already saved to subscription table in database,
        # as it can only be saved once per parent organisation account.
        subscription = Subscription.objects.select_related('product').filter(product=id)

        # If customer already has this product then do not add it to Cart.
        if subscription:
            quantity = 0
            messages.add_message(request, messages.INFO,
                                 'Product not added to Cart. This subscription is already on your account!')
    else:
        # Otherwise, check if the Cart product is a base product.
        if is_base_product:
            subscription = Subscription.objects.select_related('product').get(product__is_base_product=True)
            if subscription:
                if subscription.product.number_of_users > product.number_of_users:
                    # If customer already has a subscription product with a lower number of users then do
                    # not add it to Cart.
                    messages.add_message(request, messages.INFO, 'Base product not added to Cart. You already have a '
                                                                 + str(subscription.product.number_of_users) +
                                                                 '-user subscription on your account! '
                                                                 'Downgrades are only possible through our '
                                                                 'Sales Department. Please contact them on '
                                                                 '0800 1234567.')
                    quantity = 0
                else:
                    # Otherwise put subscription in the Cart but indicate that product is an upgrade.
                    if id not in cart:
                        total_quantity = quantity
                        user_count = product.number_of_users * total_quantity
                        messages.add_message(request, messages.INFO, 'Base product upgrade to '
                                                                     + str(user_count) +
                                                                     '-users added to Cart. You currently '
                                                                     'have a '
                                                                     + str(subscription.product.number_of_users) +
                                                                     '-user subscription on your account.')
    if id in cart:
        # If product is already in cart..
        if max_product_quantity == 1 and int(product.id) == int(id):
            # If a single item product with the same id already exists in the cart then do not update the quantity.
            messages.add_message(request, messages.INFO, 'Product is already in Cart. Only one item of '
                                                         'this product is allowed!')
        else:
            # Otherwise, UPDATE the quantity of the product in the Cart.
            cart[id] = int(cart[id]) + quantity
    else:
        # Otherwise ADD the product to the Cart along with the quantity selected.
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
