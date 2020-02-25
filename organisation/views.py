from django.shortcuts import render
from .models import Organisation

# Create your views here.
def all_organisations(request):
    """ Get all the organisations from the database. """
    organisations = Organisation.objects.all()
    return render(request, "organisations.html", {"organisations": organisations})