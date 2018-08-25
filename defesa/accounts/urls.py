from django.conf.urls import patterns, include, url
from defesa.accounts.views import PerfilCreateView

urlpatterns = patterns('',
    # Examples:
    url(r'^entrar/$', 'defesa.accounts.views.meu_login', name='login'),
    url(r'^sair/$', 'django.contrib.auth.views.logout', {'next_page': 'accounts:login'}, name='logout'),
    url(r'^cadastro/$', 'defesa.accounts.views.cadastro', name='cadastro'),
    url(r'^cadastro/novo-perfil/$', PerfilCreateView.as_view(), name='novo_perfil'),
    url(r'^editar/$', 'defesa.accounts.views.editar', name='editar'),
    url(r'^editar-senha/$', 'defesa.accounts.views.editar_senha', name='editar_senha'),
    url(r'^nova-senha/$', 'defesa.accounts.views.reset_senha', name='reset_senha'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', 'defesa.accounts.views.reset_senha_confirm', name='reset_senha_confirm'),
)
