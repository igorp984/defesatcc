# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180804_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='perfil',
            field=models.ForeignKey(related_name='perfil', verbose_name=b'Perfil', to='accounts.Perfil'),
        ),
    ]
