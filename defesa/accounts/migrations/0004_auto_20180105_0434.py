# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_novasenha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novasenha',
            name='user',
            field=models.ForeignKey(related_name='resets', verbose_name=b'Usu\xc3\xa1rio', to=settings.AUTH_USER_MODEL),
        ),
    ]
