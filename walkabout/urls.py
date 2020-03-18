"""walkabout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from django.views.generic import RedirectView
from accounts import urls as urls_accounts
from organisation import urls as urls_organisation
from .settings import MEDIA_ROOT

#from organisation.views import OrganisationDelete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='organisation/')),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^organisation/', include(urls_organisation)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
#    url(r'^organisation/(?P<pk>\d+)/delete/$', OrganisationDelete.as_view(), name='delete_organisation'),
]
