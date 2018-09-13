# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(unique=True, max_length=100, verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('nivel_acesso', models.CharField(default=b'baixo', max_length=6, choices=[(b'baixo', b'Baixo'), (b'medio', b'M\xc3\xa9dio'), (b'Alto', b'Alto')])),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
            },
        ),
        migrations.AddField(
            model_name='usuario',
            name='perfil',
            field=models.ForeignKey(related_name='perfil', verbose_name=b'Perfil', to='accounts.Perfil', null=True),
        ),
    ]
