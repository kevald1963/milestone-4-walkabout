from django.shortcuts import render
from .models import Organisation

# Create your views here.
def all_organisations(request):
    """ Get all the organisations from the database. """
    organisations = Organisation.objects.all()
    return render(request, "organisation.html", {"organisations": organisations})

def edit_organisation(request):
    """ Get the selected organisations from the database for editing. """
    organisation = Organisation.objects.all()
    return render(request, "edit_organisation.html", {"organisation": organisation})
