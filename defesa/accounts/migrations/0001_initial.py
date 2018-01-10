# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'o nome de usuário só pode conter letras, digitos os os seguintes caracteres @ . + - _', 'invalid')], max_length=30, verbose_name='Nome do Usuário', unique=True)),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail', unique=True)),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('is_active', models.BooleanField(verbose_name='Está ativo?', default=True)),
                ('is_staff', models.BooleanField(verbose_name='É admin', default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')),
                ('groups', models.ManyToManyField(related_name='user_set', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, related_query_name='user', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.', blank=True, related_query_name='user', verbose_name='user permissions')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('key', models.CharField(max_length=100, verbose_name='Chave', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('confirmed', models.BooleanField(verbose_name='Confirmado?', default=False)),
                ('user', models.ForeignKey(related_name='resets', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Novas Senhas',
                'verbose_name': 'Nova Senha',
            },
        ),
    ]
