from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('defesa.core.urls', namespace='core')),
    url(r'^', include('defesa.trabalhos.urls', namespace='trabalhos')),
    url(r'^admin/', include(admin.site.urls)),
)
