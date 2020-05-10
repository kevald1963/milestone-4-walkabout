from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import EditOrganisationForm
from .models import Organisation


# Create your views here.
def all_organisations(request):
    """
    Get all the organisations from the database, ordered by is_parent flag so that parent organisation
    is always shown at top of the page.
    """
    organisations = Organisation.objects.all().order_by('-is_parent')

    return render(request, "organisations.html", {"organisations": organisations})


def organisation_detail(request, pk):
    """
    A view that returns a single organisation's details based on its primary key
    and renders it to the 'organisation_detail.html' template.
    Returns a 404 error if the organisation is not found.
    """
    organisation = get_object_or_404(Organisation, pk=pk)
    return render(request, "organisation_detail.html", {'organisation': organisation})


def create_or_edit_organisation(request, pk=None):
    """
    A view to create or edit an organisation depending on whether its
    primary key is null or not.
    """
    organisation = get_object_or_404(Organisation, pk=pk) if pk else None
    if request.method == 'POST':
        form = EditOrganisationForm(request.POST, request.FILES, instance=organisation)
        if form.is_valid():
            form.instance.updated_by = request.user
            form.save()
            return redirect(all_organisations)
    else:
        form = EditOrganisationForm(instance=organisation)

    if organisation is None:
        # If no data found then invoke page to add organisation.
        operation_type = "add"
    else:
        # Otherwise invoke page to edit organisation.
        operation_type = "edit"

    return render(request, operation_type + '_organisation.html', {'form': form})


class OrganisationDelete(DeleteView):
    """
    Delete the organisation and return to Organisations page after delete confirmation.
    """
    model = Organisation
    template_name = 'organisation_confirm_delete.html'
    success_url = reverse_lazy('all_organisations')
