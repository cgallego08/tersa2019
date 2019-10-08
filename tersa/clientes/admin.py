from django.contrib import admin
from .models import Cliente, TipoCliente
from import_export.admin import ImportExportModelAdmin

@admin.register(Cliente, TipoCliente)
class ClienteAdmin(ImportExportModelAdmin):
    search_fields = ['Cliente']
    pass



# Register your models here.


