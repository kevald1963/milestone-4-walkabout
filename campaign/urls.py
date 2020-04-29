from django.conf.urls import url
from .views import all_campaigns


urlpatterns = [
    url(r'^campaigns/$', all_campaigns, name="all_campaigns"),
]
