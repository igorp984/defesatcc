from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    url(r'^(?P<pk>\d+)', views.EnviaEmailParticipacaoBanca.as_view(), name='email_participacao_banca'),
    url(r'^resposta-participacao-banca/(?P<key>\w+)/$', views.confirma_participacao_banca, name='confirma_participacao_banca'),
]