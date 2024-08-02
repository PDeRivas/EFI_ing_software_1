from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length = 50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Paises"

class Fuel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Combustible"
        verbose_name_plural = "Combustibles"

class Nameplate(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"

class Traction(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tracción"
        verbose_name_plural = "Tracciones"

class Transmission(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Transmisión"
        verbose_name_plural = "Transmisiones"

class Car(models.Model):
    year = models.IntegerField(verbose_name='Año')
    doors = models.IntegerField(verbose_name='Cantidad de Puertas')
    used = models.BooleanField(verbose_name='Usado')
    km = models.IntegerField(blank=True, null=True, verbose_name='Cantidad de Kilometros')
    cylinders = models.IntegerField(verbose_name='Cilindros', blank=True, null=True)
    price = models.IntegerField(verbose_name='Precio en dolares', blank=True, null=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='pais',
        verbose_name='País',
        null = True,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='marca',
        verbose_name='Marca',
    )
    nameplate = models.ForeignKey(
        Nameplate,
        on_delete=models.CASCADE,
        related_name='modelo',
        verbose_name='Modelo',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='categoria',
        verbose_name='Categoría',
    )
    fuel = models.ForeignKey(
        Fuel,
        on_delete=models.CASCADE,
        related_name='combustible',
        verbose_name='Combustible',
    )
    traction = models.ForeignKey(
        Traction,
        on_delete=models.CASCADE,
        related_name='traccion',
        verbose_name='Tracción',
    )
    transmission = models.ForeignKey(
        Transmission,
        on_delete=models.CASCADE,
        related_name='transmision',
        verbose_name='Transmisión',
    )

    def __str__(self):
        return f'{self.brand.name} {self.nameplate.name} {self.year}'
    
    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"

class PriceHistory(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE, 
        related_name='price_history'
    )
    price = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.car.name} - {self.price} on {self.date}'

class CarImage(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(upload_to='product_images/', null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description or f'Image of {self.product.name}'
