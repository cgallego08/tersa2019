from django.db import models
from django.utils import timezone

# Create your models here.

class Bodega(models.Model):
    nombre_bodega = models.CharField(max_length=250)
    descripcion_bodega = models.TextField()

    def __str__(self):
        return self.nombre_bodega


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=250)
    descripcion_categoria = models.TextField()

    def __str__(self):
        return self.nombre_categoria

