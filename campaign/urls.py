from django.conf.urls import url
from .views import all_campaigns, create_or_edit_campaign
from . import views

urlpatterns = [
    url(r'^campaigns/$', all_campaigns, name="all_campaigns"),
    url(r'^campaign/new/$', create_or_edit_campaign, name='new_campaign'),
    url(r'^campaign/(?P<pk>\d+)/edit/$', create_or_edit_campaign, name='edit_campaign'),
    url(r'^campaign/(?P<pk>\d+)/delete/$', views.CampaignDelete.as_view(), name='delete_campaign'),
]
