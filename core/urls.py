from django.conf.urls import include, url
from . import  views


urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^bancas_pendentes/$', views.banca_pendente, name='bancas_pendentes'),
    url(r'^agendamentos_pendentes/$', views.agendamento_pendente, name='agendamentos_pendentes'),
    url(r'^defesas_confirmadas/$', views.defesas_confirmadas, name='defesas_confirmadas'),
]
