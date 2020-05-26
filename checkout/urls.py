from django.conf.urls import url
from .views import checkout_paid, checkout_free


urlpatterns = [
    url(r'^paid/$', checkout_paid, name='checkout_paid'),
    url(r'^free/$', checkout_free, name='checkout_free'),
]
