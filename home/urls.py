from django.conf.urls import url
from .views import index, dashboard


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
]
