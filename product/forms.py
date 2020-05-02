from django import forms
from .models import Product


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'number',
            'name',
            'is_single_use_only',
            'is_base_product',
            'is_upgrade_product',
            'is_data_product',
            'max_product_quantity',
            'number_of_devices',
            'number_of_subscription_months',
            'description',
            'price',
            'image_path',
            'image',
            'image_caption',
        )
