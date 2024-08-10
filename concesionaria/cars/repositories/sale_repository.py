from typing import (
    List,
)

from cars.models import(
    Car,
    Sale,
    Country,
)

from django.contrib.auth.models import User

class SalesRepository:    
    def create(self,
               car: Car,
               buyer: User,
               credit_card_number: int,
               country: Country,
               city: str,
               postal_code: int,
               phone: int,
               date,
               time):
        car.sold = True
        car.save()
        return Sale.objects.create(
                            car=car,
                            buyer=buyer,
                            credit_card_number=credit_card_number,
                            country=country,
                            city=city,
                            postal_code=postal_code,
                            phone=phone,
                            date=date,
                            time=time)

    def get_all(self) -> List[Sale]:
        return Sale.objects.all()
