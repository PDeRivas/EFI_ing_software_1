from typing import (
    List,
)

from cars.models import(
    Car,
    CarImage,
)

class CarImagesRepository:    
    def get_all(self) -> List[CarImage]:
        return CarImage.objects.all()
    
    def filter_by_car(self, car:Car) -> List[CarImage]:
        return CarImage.objects.filter(car=car)
