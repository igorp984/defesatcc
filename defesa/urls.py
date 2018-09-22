from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^', include('core.urls', namespace='core')),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^trabalhos/', include('trabalhos.urls', namespace='trabalhos')),
    url(r'^admin/', include(admin.site.urls)),
]
