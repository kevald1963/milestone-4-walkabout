from django.conf.urls import url
from .views import all_rounds, create_or_edit_round, all_streets, create_or_edit_street, attached_streets
from .views import view_addresses, create_addresses, edit_address
from . import views


urlpatterns = [
    url(r'^rounds/$', all_rounds, name='all_rounds'),
    url(r'^round/new/$', create_or_edit_round, name='new_round'),
    url(r'^round/(?P<pk>\d+)/edit/$', create_or_edit_round, name='edit_round'),
    url(r'^round/(?P<pk>\d+)/delete/$', views.RoundDelete.as_view(), name='delete_round'),
    url(r'^round/streets/$', all_streets, name='all_streets'),
    url(r'^round/street/new/$', create_or_edit_street, name='new_street'),
    url(r'^round/street/(?P<pk>\d+)/edit/$', create_or_edit_street, name='edit_street'),
    url(r'^round/street/(?P<pk>\d+)/delete/$', views.StreetDelete.as_view(), name='delete_street'),
    url(r'^round/(?P<pk>\d+)/streets/create_addresses/$', create_addresses, name='create_addresses'),
    url(r'^round/attached_streets/(?P<pk>\d+)/edit/$', create_or_edit_street, name='edit_street'),
    url(r'^round/attached_streets/(?P<pk>\d+)/$', attached_streets, name='attached_streets'),
    url(r'^round/attached_streets/(?P<pk>\d+)/view_addresses/$', view_addresses, name='view_addresses'),
    url(r'^round/attached_streets/(?P<pk>\d+)/view_addresses/(?P<pk2>\d+)/edit/$', edit_address,
        name='edit_address'),
]
