from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)

# Create your models here.

class Usuario(AbstractBaseUser, PermissionsMixin):

	username = models.Charfield('Nome do Usuário', max_length=30, unique=True)
	email = models.EmailField('E-mail', unique=True)
	name = models.Charfield('Nome', max_length=200)
	is_active = models.BooleanField('Está ativo?', blank=True, default=True)
	is_staff = models.BooleanField('É admin', blank=True, default=False)
	date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']
