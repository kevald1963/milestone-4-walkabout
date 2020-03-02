from django import forms
from django.contrib.auth.models import Organisations
from django.core.exceptions import ValidationError

class EditOrganisationForm(forms.Form):
    name = forms.CharField()
    