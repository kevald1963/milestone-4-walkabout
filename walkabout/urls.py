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
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

from home import urls as urls_home
from accounts import urls as urls_accounts
from organisation import urls as urls_organisation
from product import urls as urls_product
from campaign import urls as urls_campaign
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from round import urls as urls_round


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='home/')),
    url(r'^home/', include(urls_home)),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^product/', include(urls_product)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^organisation/', include(urls_organisation)),
    url(r'^campaign/', include(urls_campaign)),
    url(r'^round/', include(urls_round)),
]
# if settings.DEBUG:
#     print("URLS configured to serve static and media files locally.")
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
