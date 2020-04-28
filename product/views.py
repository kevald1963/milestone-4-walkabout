from django.shortcuts import render
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Product, Discount


# Create your views here.
def all_products(request):
    products = Product.objects.all().order_by('number')
    try:
        percent = Discount.objects.values_list('percent', flat=True).get(code=1)
    except ObjectDoesNotExist:
        messages.error(request, "Error: Discount rate not found. Complementary 12.50% discount applied instead.")
        percent = 12.5

    return render(request, "products.html", {"products": products, "percent": percent})
