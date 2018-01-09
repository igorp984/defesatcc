# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import re
import django.contrib.auth.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'o nome de usuário só pode conter letras, digitos os os seguintes caracteres @ . + - _', 'invalid')], unique=True, verbose_name='Nome do Usuário', max_length=30)),
                ('email', models.EmailField(unique=True, verbose_name='E-mail', max_length=254)),
                ('name', models.CharField(verbose_name='Nome', max_length=200)),
                ('is_active', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='É admin')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')),
                ('groups', models.ManyToManyField(related_name='user_set', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', verbose_name='groups', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', blank=True, help_text='Specific permissions for this user.', related_query_name='user', verbose_name='user permissions', to='auth.Permission')),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'verbose_name': 'Usuário',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='NovaSenha',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('key', models.CharField(unique=True, verbose_name='Chave', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Confirmado?')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='resets', verbose_name='Usuário')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Novas Senhas',
                'verbose_name': 'Nova Senha',
            },
        ),
    ]
