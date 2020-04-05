from django import forms
from .models import Round, Street, Address


class EditRoundForm(forms.ModelForm):
    class Meta:
        model = Round
        fields = (
            'name',
            'description',
        )


class EditStreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = (
            'name',
            'comments',
            'round',
            'door_number_start',
            'door_number_end',
            'post_code',
        )


class EditAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            'door_number',
            'comments',
        )

