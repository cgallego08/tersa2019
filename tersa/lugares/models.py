from django.db import models

# Create your models here.
class Departamento(models.Model):
    departamento = models.CharField(max_length=250)

    def __str__(self):
        return self.departamento

class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre_ciudad