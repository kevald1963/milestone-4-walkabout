from django.shortcuts import render
from .models import Campaign


# Create your views here.
def all_campaigns(request):
    """
    Get all the campaigns from the database, ordered by active date
    """
    campaigns = Campaign.objects.all().order_by('active_date')
    return render(request, 'campaigns.html', {'campaigns': campaigns})
