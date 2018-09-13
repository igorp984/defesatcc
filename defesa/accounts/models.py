# -*- coding: utf-8 -*-
import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.conf import settings
# Create your models here.


class Titulo(models.Model):

	descricao = models.CharField('Descrição', max_length=100, unique=True)

	def __str__(self):
		return self.descricao

	class Meta:
		verbose_name = 'Titulo'
		verbose_name_plural = 'Titulos'

class Perfil(models.Model):
	
	#só da acesso ao usuário para visualizar informações de trabalhos cadastrados,
	# de se candidatar a banca e de fazer alterações nas informações do seu cadastro
	BAIXO = 'baixo'
	
	#O usuário pode cadastrar a defesa de um trabalho de sua orientação, assim como escolher a banca
	# além de ter o mesmo poder dos usuário de nível baixo
	MEDIO = 'medio'

	#O unico que pode cadastrar informações básicas no sistema como perfis de usuário e seus níveis de acesso 
	# titulos(ex: graduado, mestre, doutor...)
	# e pode adicionar usuário ao sistema
	ALTO = 'Alto'


	NIVEL_ACESSO_CHOICES = (
		(BAIXO, 'Baixo'),
		(MEDIO, 'Médio'),
		(ALTO, 'Alto'),
	)

	descricao = models.CharField('Descrição', max_length=100, unique=True)
	nivel_acesso = models.CharField(
        max_length=6,
        choices=NIVEL_ACESSO_CHOICES,
        default=BAIXO,
    )

	def __str__(self):
		return self.descricao

	def get_perfil(self, descricao):
		return Perfil.objects.filter(descricao=descricao).values('nivel_acesso')[0]['nivel_acesso']

	class Meta:
		verbose_name = 'Perfil'
		verbose_name_plural = 'Perfis'

	

class Usuario(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(
		'Nome do Usuário', max_length=30, unique=True,
		validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
			'o nome de usuário só pode conter letras, digitos os os seguintes caracteres @ . + - _', 'invalid')]
	)
	titulo = models.ForeignKey(Titulo, verbose_name='Titulação', related_name='titulo')
	perfil = models.ForeignKey(Perfil, verbose_name='Perfil', related_name='perfil')
	email = models.EmailField('E-mail', unique=True)
	name = models.CharField('Nome', max_length=200)
	is_active = models.BooleanField('Está ativo?', blank=True, default=True)
	is_staff = models.BooleanField('É admin', blank=True, default=False)
	date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return self.name or self.username

	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return str(self)

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'			

class NovaSenha(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='resets')
	key = models.CharField('Chave', max_length=100, unique=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

	def __str__(self):
		return '{0} em {1}'.format(self.user, self.created_at)

	class Meta:
		verbose_name = 'Nova Senha'
		verbose_name_plural = 'Novas Senhas'
		ordering = ['-created_at']