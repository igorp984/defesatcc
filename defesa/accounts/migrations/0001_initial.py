# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=30, verbose_name=b'Nome do Usu\xc3\xa1rio')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name=b'E-mail')),
                ('name', models.CharField(max_length=200, verbose_name=b'Nome')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Est\xc3\xa1 ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'\xc3\x89 admin')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name=b'Data de Entrada')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
