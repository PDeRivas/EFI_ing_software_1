from typing import (
    List,
    Optional,
)

from cars.models import(
    Car,
    Brand,
    Category,
    Fuel,
    Nameplate,
    Traction,
    Transmission,
)

#logger = logging.getLogger(__name__)

class CarsRepository:
    def create(self,
               brand: Brand,
               category: Category,
               fuel: Fuel,
               nameplate: Nameplate,
               traction: Traction,
               transmission: Transmission,
               year: int,
               doors: int,
               used: bool,
               km: int,
               ) -> Car.objects:
        
        return Car.objects.create(
            brand = brand,
            category = category,
            fuel = fuel,
            nameplate = nameplate,
            traction = traction,
            transmission = transmission,
            year = year,
            doors = doors,
            used = used,
            km = km,
        )
    
    def get_all(self) -> List[Car]:
        return Car.objects.all()
    
    def get_by_id(self, id: int,) -> Optional[Car]:
        try:
            product = Car.objects.get(id=id)
        except:
            product = None
        return product
    
    def filter_by_category(
            self,
            category = Category,
    ) -> List[Car]:
        return category.objects.filter(category = category)
