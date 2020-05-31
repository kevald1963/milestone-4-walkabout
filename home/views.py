from django.shortcuts import render, redirect, reverse
from campaign.models import Campaign


# Create your views here.
def index(request):
    """
    A view that displays the index page.
    """
    return render(request, "index.html")
