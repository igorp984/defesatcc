from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^entrar/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', 'django.contrib.auth.views.logout', {'next_page': 'accounts:login'}, name='logout'),
    url(r'^cadastro/$', 'defesa.accounts.views.cadastro', name='cadastro'),
    url(r'^editar/$', 'defesa.accounts.views.editar', name='editar'),
)
