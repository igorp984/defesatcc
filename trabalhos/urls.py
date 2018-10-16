from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    url(r'^cadastrar_trabalho/novo$', views.cadastrar_trabalho, name='cadastrar_trabalho'),
    url(r'^detalhe/(?P<pk>\d+)/$', views.detalhe, name='detalhe'),
    url(r'^editar/(?P<pk>\d+)/$', views.TrabalhoUpdateView.as_view(), name='editar'),
    url(r'^(?P<pk>\d+)/$', views.TrabalhoDetail.as_view(), name='deletar'),
    url(r'^agendamento/novo/(?P<pk>\d+)$', views.defesatrabalho, name='cadastrar_agendamento_defesa')
]
