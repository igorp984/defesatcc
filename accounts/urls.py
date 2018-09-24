from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
                       # Examples:
    url(r'^entrar/$', views.meu_login, name='login'),
    url(r'^sair/$', auth_views.logout, {'next_page': 'accounts:login'}, name='logout'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^cadastro/novo-perfil/$', views.PerfilCreateView.as_view(), name='novo_perfil'),
    url(r'^editar/(?P<pk>\d+)/$', views.UsuarioUpdateView.as_view(), name='editar'),
    url(r'^editar-senha/$', views.editar_senha, name='editar_senha'),
    url(r'^nova-senha/$', views.reset_senha, name='reset_senha'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.reset_senha_confirm, name='reset_senha_confirm'),
]
