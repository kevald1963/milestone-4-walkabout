from django import forms
from .models import Organisation


class EditOrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = (
            'name',
            'description',
            'contact_name',
            'is_parent',
            'logo_text',
            'glyphicon_name',
            'image_path',
            'image',
            'image_caption',
            'address_1',
            'address_2',
            'address_3',
            'town_or_city',
            'post_code',
            'email_address',
            'landline_number',
            'mobile_number',
        )
