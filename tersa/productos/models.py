from django.db import models
from categorias.models import Categoria, Bodega

# Create your models here.

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=250)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    codigo_producto = models.CharField(max_length=255, unique=True,)
    precio = models.FloatField()
    cantidad_stock = models.IntegerField(default=0)
    descripcion_producto = models.TextField()

    def __str__(self):
        return self.nombre_producto