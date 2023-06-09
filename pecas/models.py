from __future__ import unicode_literals

from django.db import models


class Estado(models.Model):
    uf =  models.CharField(max_length=2)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.uf

