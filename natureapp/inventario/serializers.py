from rest_framework import serializers
from .models import Categoria
from .models import Producto
from .validators import validation_nombre

from .models import Supermercado
from .models import Informacion

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
        
class SupermercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supermercado
        fields = "__all__"

class InformacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informacion
        fields = "__all__"

class ReporteProductosSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    productos = ProductoSerializer(many=True)


class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=20, validators=[validation_nombre])
    body = serializers.CharField(max_length=255)