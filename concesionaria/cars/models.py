from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

#Marca del auto
class Brand(models.Model):
    name = models.CharField(max_length = 50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

#Tipo de auto
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

#País de origen
class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Paises"

#Tipo de combustible
class Fuel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Combustible"
        verbose_name_plural = "Combustibles"

#Modelo del auto
class Nameplate(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"

#Tipo de tracción
class Traction(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre',)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tracción"
        verbose_name_plural = "Tracciones"

#Forma de transmisión
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
    cylinders = models.CharField(max_length=5, verbose_name='Cilindros', blank=True, null=True)
    price = models.IntegerField(verbose_name='Precio en dólares', blank=True, null=True)
    sold = models.BooleanField(verbose_name='Vendido', default=False)
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
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True)

    def __str__(self):
        return f'{self.brand.name} {self.nameplate.name} {self.year}'
    
    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"

class CarImage(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='Auto',
        verbose_name='Autos',
    )
    image = models.ImageField(upload_to='car_images/', null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description or f'Imagen de {self.car}'
    
    class Meta:
            verbose_name = "Imagen"
            verbose_name_plural = "Imagenes"

class Comment(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='comentario',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.author.username} sobre {self.car}'

class Review(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='review',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()

    def __str__(self):
        return f'review de {self.author.username} sobre {self.car}. Rating de: {self.rating}'
