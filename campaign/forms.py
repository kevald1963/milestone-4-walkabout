from django import forms
from .models import Campaign


class EditCampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = (
            'id',
            'name',
            'description',
            'campaign_lead',
            'organisation',
            'campaign_type',
            'rounds',
            'active_date',
            'inactive_date',
        )
