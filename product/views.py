from django.shortcuts import render
from .models import Product, Discount


# Create your views here.
def all_products(request):
    products = Product.objects.all().order_by('number')
    discount = Discount.objects.get(code=1)
    return render(request, "products.html", {"products": products, "discount": discount})
