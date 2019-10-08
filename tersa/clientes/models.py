from django.db import models
from lugares.models import Departamento, Ciudad
# Create your models here.
class TipoCliente(models.Model):
    tipo_cliente = models.CharField(max_length=250)
    descripcion_cliente = models.TextField()

    def __str__(self):
        return self.tipo_cliente


class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=250)
    cedula_nit = models.BigIntegerField()
    telefono = models.BigIntegerField()
    correo_electronico = models.EmailField(blank=True, default="")
    direccion = models.CharField(max_length=250)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_cliente