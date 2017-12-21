from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^entrar/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^cadastro/$', 'defesa.accounts.views.cadastro', name='cadastro'),
    
)
