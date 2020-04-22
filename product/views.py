from django.shortcuts import render
from .models import Product, Discount


# Create your views here.
def all_products(request):
    products = Product.objects.all().order_by('number')
    percent = Discount.objects.values_list('percent', flat=True).get(code=1)
    return render(request, "products.html", {"products": products, "percent": percent})
