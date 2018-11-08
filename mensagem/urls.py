from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    url(r'^(?P<pk>\d+)', views.EnviaEmailParticipacaoBanca.as_view(), name='email_participacao_banca'),
    url(r'^confirma-participacao-banca/(?P<key>\w+)/$', views.confirmada_participacao_banca, name='confirmada_participacao_banca'),
    url(r'^rejeita-participacao-banca/(?P<key>\w+)/$', views.rejeitada_participacao_banca, name='rejeitada_participacao_banca'),
]