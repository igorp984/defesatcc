# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-19 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensagem', '0005_auto_20181019_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailparticipacaobanca',
            name='visualizada',
            field=models.DateField(blank=True, verbose_name='Visualizada em'),
        ),
    ]