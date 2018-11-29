from django.conf.urls import url
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^entrar/$', views.meu_login, name='login'),
    url(r'^sair/$', auth_views.logout, {'next_page': 'accounts:login'}, name='logout'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^cadastro/(?P<key>\w*)/$', views.cadastro, name='cadastro'),
    url(r'^cadastro/novo-perfil/$', views.PerfilCreateView.as_view(), name='novo_perfil'),
    url(r'^editar/(?P<pk>\d+)/$', views.UsuarioUpdateView.as_view(), name='editar'),
    url(r'^(?P<pk>\d+)/$', views.UsuarioUpdateApiView.as_view(), name='editar_api'),
    url(r'^editar-senha/$', views.editar_senha, name='editar_senha'),
    url(r'^nova-senha/$', views.reset_senha, name='reset_senha'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.reset_senha_confirm, name='reset_senha_confirm'),
    url(r'^certificado/orientador/(?P<pk>\d+)/$', views.CertificadoOrientadorPDFView.as_view(), name='certificado_orientador'),
    url(r'^certificado/avaliador/(?P<pk>\d+)/(?P<user_id>\d+)/$', views.CertificadoAvaliadorPDFView.as_view(), name='certificado_avaliador'),
]

urlpatterns = format_suffix_patterns(urlpatterns)