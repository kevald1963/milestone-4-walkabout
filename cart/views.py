from django.shortcuts import render, reverse, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from product.models import Product
from organisation.models import Subscription


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
    is_data_product = product.is_data_product

    # ====================================================================================================
    # Products can either be BASE or DATA products. A data product CANNOT be bought without purchasing a
    # base product first. The same base product CANNOT be bought twice, however it can be upgraded to one
    # with a higher number of devices / longer subscription duration. Downgrades are possible but are not
    # handled by the system. Customers are referred to the Sales Team instead.
    # ====================================================================================================

    if max_product_quantity == 1:
        # ================================================================================================
        # Check if product with a single item quantity is already saved to subscription table in database,
        # as it can only be saved once per parent organisation account.
        # ================================================================================================
        subscription = Subscription.objects.select_related('product').filter(product=id)

        # If customer already has this product then do not add it to Cart, but tell customer why!
        # Set quantity to zero.
        if subscription:
            quantity = 0
            messages.add_message(request, messages.INFO,
                                 'Product not added to Cart. This product is already subscribed to!')
    else:
        if is_base_product:
            # =================================================================================
            # If the Cart product is a base product, then see if a subscription for it already
            # exists.
            # =================================================================================
            try:
                subscription = Subscription.objects.select_related('product').get(product__is_base_product=True)
                if subscription:
                    if subscription.product.number_of_devices > product.number_of_devices:
                        # =====================================================================================
                        # If customer already owns a subscription product with a higher number of devices then
                        # do not add this product to the Cart. Set quantity to zero.
                        # =====================================================================================
                        quantity = 0
                        messages.add_message(request, messages.INFO, 'Base product not added to Cart. You already have '
                                                                     'a '
                                                                     + str(subscription.product.number_of_devices) +
                                                                     '-device subscription on your account! '
                                                                     'Downgrades are only possible through our '
                                                                     'Sales Department. Please contact them on '
                                                                     '0800 1234567.')
                    else:
                        # Otherwise put subscription in the Cart but indicate that product is an upgrade.
                        if id not in cart:
                            total_quantity = quantity
                            devices_count = product.number_of_devices * total_quantity
                            messages.add_message(request, messages.INFO, 'Base product upgrade to '
                                                                         + str(devices_count) +
                                                                         '-devices added to Cart. You currently '
                                                                         'have a '
                                                                         + str(subscription.product.number_of_devices) +
                                                                         '-device subscription on your account.')
            except ObjectDoesNotExist:
                # if no subscription found, then add to the Cart and inform user.
                messages.error(request, "Base subscription product added to Cart.")
        else:
            if is_data_product:
                # =================================================================================
                # If the Cart product is a data product, then check if a subscription for a base
                # product already exists.
                # =================================================================================
                try:
                    Subscription.objects.select_related('product').get(product__is_base_product=True)
                except ObjectDoesNotExist:
                    # ========================================================================================
                    # If no subscription found, then check if a base item already in the Cart. If not in cart
                    #  either then inform user they will also need to add a base product.
                    # ========================================================================================
                    for new_id, qty in cart.items():
                        product = Product.objects.get(id=new_id)
                        if not product.is_base_product:
                            messages.error(request, "Please add a base product to go with this data product. "
                                                    "You have no base product registered on system.")

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
