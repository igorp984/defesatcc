# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(unique=True, max_length=30, verbose_name=b'Nome do Usu\xc3\xa1rio', validators=[django.core.validators.RegexValidator(re.compile(b'^[\\w.@+-]+$'), b'o nome de usu\xc3\xa1rio s\xc3\xb3 pode conter letras, digitos os os seguintes caracteres @ . + - _', b'invalid')]),
        ),
    ]
