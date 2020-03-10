from django.conf.urls import url, include
from .views import all_organisations, create_or_edit_organisation


urlpatterns = [
    url(r'^$', all_organisations, name="organisations"),
    url(r'^new/$', create_or_edit_organisation, name='new_organisation'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_organisation, name='edit_organisation'),
]