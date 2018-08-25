from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('defesa.core.urls', namespace='core')),
    url(r'^conta/', include('defesa.accounts.urls', namespace='accounts')),
    url(r'^trabalhos/', include('defesa.trabalhos.urls', namespace='trabalhos')),
    url(r'^admin/', include(admin.site.urls)),
)
