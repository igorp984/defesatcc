# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from accounts.models import Usuario
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError

# Create your models here.
@python_2_unicode_compatible
class Trabalhos(models.Model):

	titulo = models.CharField('Título', max_length=250)
	keywords = models.CharField('Palavras Chaves', max_length=150)
	autor = models.CharField('Autor', max_length=250)
	orientador = models.ForeignKey(Usuario, verbose_name='orientador', related_name='orientador')
	co_orientador = models.CharField('Co Orientador', max_length=250, blank=True)
	resumo = models.TextField('Resumo', blank=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.titulo



class DefesaTrabalho(models.Model):
	BANCA_AVALIADORA_PENDENTE = 'pendente_banca_avaliadora'
	AGENDADO = 'agendado'

	STATUS_CHOICES = (
		(BANCA_AVALIADORA_PENDENTE, 'Aguardando reposta ao convite para banca'),
		(AGENDADO, 'Agendado'),
	)

	local = models.CharField('Local', max_length=250)
	data = models.DateField('Data')
	hora = models.TimeField('Horário')
	trabalho = models.ForeignKey(Trabalhos, verbose_name='trabalho', related_name='bancatrabalhos')
	banca = models.ManyToManyField(Usuario, through='BancaTrabalho')
	status = models.CharField(
		'Status', max_length=30,
		choices=STATUS_CHOICES,
		default=BANCA_AVALIADORA_PENDENTE)

class BancaTrabalho(models.Model):

	ACEITO_PELO_ORIENTADOR = 'aceito_pelo_orientador'
	ACEITO_PELO_AVALIADOR = 'aceito_pelo_avaliador'
	NEGADO_PELO_ORIENTADOR = 'negado_pelo_orientador'
	NEGADO_PELO_AVALIADOR = 'negado_pelo_avaliador'
	PENDENTE_DE_RESPOSTA = 'pendentes_de_resposta'

	STATUS_CONVITE_CHOICES = (
		(ACEITO_PELO_ORIENTADOR, 'aceito_pelo_orientador'),
		(ACEITO_PELO_AVALIADOR,'aceito_pelo_avaliador'),
		(NEGADO_PELO_ORIENTADOR,'negado_pelo_orientador'),
		(NEGADO_PELO_AVALIADOR,'negado_pelo_avaliador'),
		(PENDENTE_DE_RESPOSTA,'pendentes_de_resposta'),
	)

	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	defesa_trabalho = models.ForeignKey(DefesaTrabalho, on_delete=models.CASCADE)
	status = models.CharField(
		'Status', max_length=30,
		choices=STATUS_CONVITE_CHOICES,
		default=PENDENTE_DE_RESPOSTA
	)





