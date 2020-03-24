from django import forms
from .models import Round, Street


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
