from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    url(r'^(?P<pk>\d+)', views.EnviaEmailParticipacaoBanca.as_view(), name='email_participacao_banca'),
    url(r'^resposta-participacao-banca/(?P<pk>\d+)', views.resposta_participacao_banca, name='resposta_participacao_banca'),
]