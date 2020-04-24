from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2041)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Expiry month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Expiry Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput, required=False)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'name',
            'address_1',
            'address_2',
            'address_3',
            'town_or_city',
            'post_code',
            'email_address',
            'mobile_number',
        )
