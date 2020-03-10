from django import forms
from .models import Organisation
from django.core.exceptions import ValidationError


class EditOrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = (
            'name',
            'description',
            'is_parent',
            'logo_text',
            'glyphicon_name',
            'image_path',
            'image',
            'image_caption',
            'address_1',
            'address_2',
            'address_3',
            'address_4',
            'post_code',
            'email_address',
        )
