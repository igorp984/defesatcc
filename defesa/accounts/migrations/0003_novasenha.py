# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180105_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='NovaSenha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=100, verbose_name=b'Chave')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
                ('confirmed', models.BooleanField(default=False, verbose_name=b'Confirmado?')),
                ('user', models.ForeignKey(verbose_name=b'Usu\xc3\xa1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Nova Senha',
                'verbose_name_plural': 'Novas Senhas',
            },
        ),
    ]
