from django.conf.urls import url
from .views import index, dashboard, assign_user_to_campaign, campaign_tasks


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^dashboard/assign_user_to_campaign/(?P<pk>\d+)/$', assign_user_to_campaign, name='assign_user_to_campaign'),
    url(r'^campaign_tasks/(?P<pk>\d+)/$', campaign_tasks, name='campaign_tasks'),
]
