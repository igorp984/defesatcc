# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from django.db import models
from accounts.models import Usuario
from trabalhos.models import Trabalhos

# Create your models here.


class EmailParticipacaoBanca(models.Model):

    remetente = models.ForeignKey(Usuario, verbose_name='Usuarios', related_name='usuarios')
    destinatario = models.ForeignKey(Usuario,verbose_name='Usuario', related_name='usuario')
    trabalho = models.ForeignKey(Trabalhos, verbose_name='Trabalhos', related_name='trabalhos')
    key = models.CharField('Chave', max_length=100, unique=True)
    visualizada = models.DateField('Visualizada em', null=True, blank=True)
    tipo = models.CharField('Tipo', max_length=30)

