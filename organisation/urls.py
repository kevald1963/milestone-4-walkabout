from django.conf.urls import url
from .views import all_organisations, organisation_detail, create_or_edit_organisation
from . import views


urlpatterns = [
    url(r'^$', all_organisations, name="all_organisations"),
    url(r'^(?P<pk>\d+)/$', organisation_detail, name='organisation_detail'),
    url(r'^new/$', create_or_edit_organisation, name='new_organisation'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_organisation, name='edit_organisation'),
    url(r'^(?P<pk>\d+)/delete/$', views.OrganisationDelete.as_view(), name='delete_organisation'),
]
