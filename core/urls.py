from django.conf.urls import include, url
from . import  views


urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),
]
