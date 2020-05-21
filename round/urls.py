from django.conf.urls import url
from .views import all_rounds, create_or_edit_round, all_streets, create_or_edit_street, linked_streets
from .views import view_addresses, create_addresses, edit_address
from . import views


urlpatterns = [
    url(r'^$', all_rounds, name='all_rounds'),
    url(r'^new/$', create_or_edit_round, name='new_round'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_round, name='edit_round'),
    url(r'^(?P<pk>\d+)/delete/$', views.RoundDelete.as_view(), name='delete_round'),
    url(r'^streets/$', all_streets, name='all_streets'),
    url(r'^street/new/$', create_or_edit_street, name='new_street'),
    url(r'^street/(?P<pk>\d+)/edit/$', create_or_edit_street, name='edit_street'),
    url(r'^street/(?P<pk>\d+)/delete/$', views.StreetDelete.as_view(), name='delete_street'),
    url(r'^(?P<pk>\d+)/streets/create_addresses/$', create_addresses, name='create_addresses'),
    url(r'^linked_streets/(?P<pk>\d+)/edit/$', create_or_edit_street, name='edit_street'),
    url(r'^linked_streets/(?P<pk>\d+)/$', linked_streets, name='linked_streets'),
    url(r'^linked_streets/(?P<pk>\d+)/view_addresses/$', view_addresses, name='view_addresses'),
    url(r'^linked_streets/(?P<pk>\d+)/view_addresses/(?P<pk2>\d+)/edit/$', edit_address,
        name='edit_address'),
    url(r'^linked_streets/(?P<pk>\d+)/view_addresses/delete/$', views.AddressDelete.as_view(), name='delete_address'),
]
