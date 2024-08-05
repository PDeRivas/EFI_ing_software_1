import csv

from django.core.management.base import BaseCommand, CommandParser

from cars.repositories.car_repository import CarsRepository

class Command(BaseCommand):
    help = "Borrar todos los autos de la base de datos"

    def handle(self, *args, **kwargs) -> str | None:
        self.stdout.write(self.style.WARNING('Iniciando Eliminacion de autos'))
        repo = CarsRepository()
        cars = repo.get_all()
        for car in cars:
            repo.delete(car)

        self.stdout.write(self.style.WARNING('Finalizada la Eliminación'))