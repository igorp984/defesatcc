# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Trabalhos(models.Model):

	titulo = models.CharField('Título', max_length=150)
	keywords = models.CharField('Palavras Chaves', max_length=150)
	autor = models.CharField('Autor', max_length=150)
	orientador = models.CharField('Orientador', max_length=150)
	co_orientador = models.CharField('Co Orientador', max_length=150, blank=True)
	resumo = models.TextField('Resumo', blank=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

