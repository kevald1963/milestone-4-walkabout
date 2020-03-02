from django import forms
from django.core.exceptions import ValidationError

class EditOrganisationForm(forms.Form):
    name = forms.CharField()
    