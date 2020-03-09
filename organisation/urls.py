from django.conf.urls import url, include
from .views import all_organisations

urlpatterns = [
    url(r'^$', all_organisations, name="organisations"),
]