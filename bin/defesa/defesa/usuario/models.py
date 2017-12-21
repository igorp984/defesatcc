# -*- coding: utf-8 -*-
from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

		usuario = models.CharField('Login', max_length=50, unique=True)
		email = models.CharField('E-mail', max_length=50, unique=True)
		nome = models.CharField('Nome', max_length=150)
		matricula = models.IntegerField('Matricula', max_length=200)
		is_active = models.BooleanField('Está ativo?', blank=True, default=True)
		is_staff = models.BooleanField('É da equipe', blank=True, default=False)
		date_joined = models.DateTimeField('Data de Cadastro', auto_now_add=True)
		date_logged = models.DateTimeField('Data do Login', auto_now=True)

		objects = UserManager()

		USERNAME_FIELD = 'usuario'
		REQUIRED_FIELDS = ['email']

		def __str__(self):
			return self.nome

		def get_short_name(self):
			return self.usuario

		def get_full_name(self):
			return str(self)

		class Meta:
			verbose_name = 'Usuário'
			verbose_name_plural = 'Usuários'
