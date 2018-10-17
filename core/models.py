from django.db import models
# Create your models here.

class Teste(models.Model):
    teste = models.CharField('Teste', max_length=30)


    class Meta:
        verbose_name = 'Teste'
        verbose_name_plural = 'Teste'
