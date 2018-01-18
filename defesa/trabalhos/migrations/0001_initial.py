# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabalhos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=150, verbose_name=b'T\xc3\xadtulo')),
                ('keywords', models.CharField(max_length=150, verbose_name=b'Palavras Chaves')),
                ('autor', models.CharField(max_length=150, verbose_name=b'Autor')),
                ('orientador', models.CharField(max_length=150, verbose_name=b'Orientador')),
                ('co_orientador', models.CharField(max_length=150, verbose_name=b'Co Orientador', blank=True)),
                ('resumo', models.TextField(verbose_name=b'Resumo', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Atualizado em')),
            ],
        ),
    ]
