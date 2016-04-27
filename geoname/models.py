from __future__ import unicode_literals

from django.db import models


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Ciudades"

    def __unicode__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad)

    def __str__(self):
        return str(self.nombre)
