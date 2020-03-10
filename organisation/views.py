from django.shortcuts import render, get_object_or_404, redirect
from .forms import EditOrganisationForm
from .models import Organisation

# Create your views here.
def all_organisations(request):
    """ Get all the organisations from the database. """
    organisations = Organisation.objects.all().order_by('-is_parent')

    return render(request, "organisations.html", {"organisations": organisations})

def create_or_edit_organisation(request, pk):
    """
    A view to allows us to create or edit an organisation depending on whether the organisation ID
    is null or otherwise.
    """
    organisation = get_object_or_404(Organisation, pk=pk) if pk else None
    if request.method == 'POST':
        form = EditOrganisationForm(request.POST, request.FILES, instance=organisation)
        if form.is_valid():
            org = form.save()
            return redirect(all_organisations)
    else:
        form = EditOrganisationForm(instance=organisation)

    return render(request, 'edit_organisation.html', {'form': form})
