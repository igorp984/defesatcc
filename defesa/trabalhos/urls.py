from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    url(r'^cadastrar_trabalho/novo$', 'defesa.trabalhos.views.cadastrar_trabalho', name='cadastrar_trabalho'),
    url(r'^detalhe/(?P<pk>\d+)/$', 'defesa.trabalhos.views.detalhe', name='detalhe'),
    url(r'^editar/(?P<pk>\d+)/$', views.TrabalhoUpdateView.as_view(), name='editar'), 
    
)
