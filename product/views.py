from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all().order_by('number')
    return render(request, "products.html", {"products": products})
