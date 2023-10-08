from django.db import models
from .validators import validar_num
from .validators import validation_categoria
from django.core.validators import EmailValidator

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validation_categoria,])
    def __str__(self):
        return self.nombre
    
class Supermercado(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validation_categoria,])
    def __str__(self):
        return self.nombre
    
class Informacion(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validation_categoria,])
    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("reporte_cantidad", "Visualizar la cantidad reporte"),
            ("reporte_detalle", "Reporte detallado de cantidades"),
        ]

class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades (precio Bs)'
    KG = 'kg', 'Kilogramos (precio Bs por kilo)'
    LT = 'lt', 'Litros (precio Bs por litro)'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_num])
    unidades = models.CharField(
        max_length=2,
        choices=ProductUnits.choices,
        default=ProductUnits.UNITS
    )
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
# Create your models here.
