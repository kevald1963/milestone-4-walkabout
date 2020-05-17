from django.shortcuts import render
from campaign.models import Campaign


# Create your views here.
def index(request):
    """
    A view that displays the index page.
    """
    return render(request, "index.html")


def dashboard(request):
    """
    A view that displays the dashboard page. The dashboard shows the campaign tasks
    assigned to each Agent.
    """
    # Select all active campaigns with attached rounds
    campaigns = Campaign.objects.all().filter(inactive_date__isnull=True).order_by('id')
    print('campaigns = ' + str(campaigns))

    return render(request, "dashboard.html",  {'campaigns': campaigns})
