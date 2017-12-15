from django.db import models

from defesa.trabalhos.models import Trabalhos
# Create your models here.

class Defesa(models.Model):
	banca = models.CharField('Banca', max_length=200)
	trabalhos = models.ManyToManyField(Trabalhos)
		