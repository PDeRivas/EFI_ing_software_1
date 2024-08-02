from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from cars.models import(
    Car,
    Brand,
    Category,
    Country,
    Fuel,
    Nameplate,
    Traction,
    Transmission,
)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Nameplate)
class NameplateAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Traction)
class Traction(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Transmission)
class Transmission(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand',
                    'category',
                    'nameplate',
                    'year',
                    'fuel',
                    'traction',
                    'transmission',
                    )
    
    
