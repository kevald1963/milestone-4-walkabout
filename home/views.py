from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from campaign.models import Campaign
from round.models import Street


# Create your views here.
def index(request):
    """
    A view that displays the index page.
    """
    return render(request, "index.html")


def start_tasks(request, pk):
    """
    A view that gets the campaign and round data to physically start the campaign.
    Called from the Dashboard page.
    """
    campaign = Campaign.objects.get(pk=pk)
    return render(request, "start_tasks.html", {'campaign': campaign})
