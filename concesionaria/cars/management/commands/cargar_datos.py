import csv

from django.core.management.base import BaseCommand, CommandParser

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

class Command(BaseCommand):
    help = "Cargar autos desde un archivo .csv. Se necesitan los siguientes datos: Marca \n Modelo \n AniodeFabricacion \n CantidaddePuertas \n Cilindrada \n TipodeCombustible \n PaisdeFabricacion \n Precioendolares \n Usado \n Kilometros \n Categoria \n Traccion \n Transmision"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'archivo_csv',
            type=str,
            help="Archivo csv desde donde se va a cargar los autos"
        )

    def handle(self, *args, **kwargs) -> str | None:
        self.stdout.write(self.style.WARNING('Iniciando Carga de autos'))
        csv_file = kwargs['archivo_csv']
        
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                brand_name = row['Marca']
                brand = Brand.objects.get_or_create(name=brand_name)[0]
                category_name = row['Categoria']
                category = Category.objects.get_or_create(name=category_name)[0]
                country_name = row['PaisdeFabricacion']
                country = Country.objects.get_or_create(name=country_name)[0]
                fuel_name = row['TipodeCombustible']
                fuel = Fuel.objects.get_or_create(name=fuel_name)[0]
                nameplate_name = row['Modelo']
                nameplate = Nameplate.objects.get_or_create(name=nameplate_name)[0]
                traction_name = row['Traccion']
                traction = Traction.objects.get_or_create(name=traction_name)[0]
                transmission_name = row['Transmision']
                transmission = Transmission.objects.get_or_create(name=transmission_name)[0]
                year = row['AniodeFabricacion']
                doors = row['CantidaddePuertas']
                cylinders = row['Cilindrada']
                price = row['Precioendolares']
                used = row['Usado']
                km = row['Kilometros']
                Car.objects.create(year=year,
                                   doors=doors,
                                   cylinders=cylinders,
                                   price=price,
                                   used=used,
                                   km=km,
                                   brand=brand,
                                   category=category,
                                   country=country,
                                   fuel=fuel,
                                   nameplate=nameplate,
                                   traction=traction,
                                   transmission=transmission)

        self.stdout.write(self.style.WARNING('Finalizada la carga'))