from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from .forms import EditProductForm
from .models import Product, Discount


# Create your views here.
def all_products(request):
    products = Product.objects.all().order_by('number')
    try:
        percent = Discount.objects.values_list('percent', flat=True).get(code=1)
    except ObjectDoesNotExist:
        messages.error(request, "Normal discount rate not found. Complementary 12.50% discount applied instead.")
        percent = 12.5

    return render(request, "products.html", {"products": products, "percent": percent})


def create_or_edit_product(request, pk=None):
    """
    A view to create or edit a product depending on whether its
    primary key is null or not.
    """
    product = get_object_or_404(Product, pk=pk) if pk else None
    if request.method == 'POST':
        form = EditProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(all_products)
    else:
        form = EditProductForm(instance=product)

    operation_type = 'edit' if product else 'add'

    return render(request, operation_type + '_product.html', {'form': form})


class ProductDelete(DeleteView):
    """
    Delete the product and return to Product page after delete confirmation.
    """
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('all_products')
