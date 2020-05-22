from django import forms
from .models import Campaign


class EditCampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = (
            'name',
            'description',
            'campaign_lead',
            'organisation',
            'campaign_type',
            'rounds',
            'assigned_users',
            'active_date',
            'inactive_date',
        )
