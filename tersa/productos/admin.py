from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Producto, Categoria, Bodega

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'categoria', 'precio', 'cantidad_stock', 'codigo_producto', 'Bodega')
    list_filter = ('categoria','precio','cantidad_stock')
    search_fields = ['nombre_producto', 'codigo_producto']


admin.site.register(Producto, ProductoAdmin)
