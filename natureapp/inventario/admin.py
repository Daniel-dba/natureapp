from django.contrib import admin
from .models import Categoria
from .models import Producto
from .models import Supermercado
from .models import Informacion
admin.site.register(Categoria)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'unidades', 'disponible')
    ordering = ['precio']
    search_fields = ['nombre']
    list_filter = ['disponible']

admin.site.register(Producto, ProductoAdmin)

class SupermercadoAdmin(admin.ModelAdmin):
    display = ('nombre')
    search_fields = ['nombre']
    
class InformacionAdmin(admin.ModelAdmin):
    display = ('nombre')
    search_fields = ['nombre']

admin.site.register(Supermercado, SupermercadoAdmin)
admin.site.register(Informacion, InformacionAdmin)


# Register your models here.
