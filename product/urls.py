from django.conf.urls import url
from .views import all_products, create_or_edit_product
from . import views


urlpatterns = [
    url(r'^products/$', all_products, name='all_products'),
    url(r'^product/new/$', create_or_edit_product, name='new_product'),
    url(r'^product/(?P<pk>\d+)/edit/$', create_or_edit_product, name='edit_product'),
    url(r'^product/(?P<pk>\d+)/delete/$', views.ProductDelete.as_view(), name='delete_product'),
]