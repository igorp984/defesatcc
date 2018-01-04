from django.conf.urls import patterns, include, url

urlpatterns = patterns('defesa.trabalhos.views',
    # Examples:
    url(r'^cadastrar_trabalho/novo$', 'cadastrar_trabalho', name='cadastrar_trabalho'),
    url(r'^trabalho/(?P<pk>\d+)/$', 'detalhe', name='detalhe'),
    
)
