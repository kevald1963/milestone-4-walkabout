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
    new_campaigns = Campaign.objects.all().filter(inactive_date__isnull=True).order_by('id')
    return render(request, "dashboard.html",  {'new_campaigns': new_campaigns})
