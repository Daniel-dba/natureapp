# Generated by Django 4.2.5 on 2023-10-08 01:53

from django.db import migrations, models
import django.db.models.deletion
import inventario.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, validators=[inventario.validators.validation_categoria])),
            ],
            options={
                'permissions': [('reporte_cantidad', 'Visualizar la cantidad reporte'), ('reporte_detalle', 'Reporte detallado de cantidades')],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, validators=[inventario.validators.validar_num])),
                ('unidades', models.CharField(choices=[('u', 'Unidades (precio Bs)'), ('kg', 'Kilogramos (precio Bs por kilo)'), ('lt', 'Litros (precio Bs por litro)')], default='u', max_length=2)),
                ('disponible', models.BooleanField(blank=True, default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.categoria')),
            ],
        ),
    ]
