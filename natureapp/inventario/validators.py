from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

def validar_num(value):
     if value  <= 0:
         raise ValidationError('%(value)s no existe precios negativos', params={'value': value})


def validation_categoria(value):
    if value == "No permitido":
        raise ValidationError("No es una opcion permitida")

def validation_nombre(value):
    if value == "Desayuno" or value == "Almuerzo" or value == "Cena":
        raise ValidationError("No es un texto permitido")