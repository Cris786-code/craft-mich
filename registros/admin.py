from django.contrib import admin
from .models import Categoria, Municipio, Producto, MensajeContacto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que se mostrarán en la lista principal del admin
    list_display = ('nombre', 'categoria', 'origen', 'precio', 'stock')
    
    # Filtros laterales
    list_filter = ('categoria', 'origen')
    
    # Barra de búsqueda (busca por nombre de producto y cruza a las tablas relacionadas)
    search_fields = ('nombre', 'categoria__nombre', 'origen__nombre')
    
    # Campos que se pueden editar directamente desde la lista sin entrar al detalle
    list_editable = ('precio', 'stock')

@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'nombre', 'email', 'fecha_envio', 'leido')
    list_filter = ('leido', 'fecha_envio')
    search_fields = ('nombre', 'email', 'asunto')
    list_editable = ('leido',)
