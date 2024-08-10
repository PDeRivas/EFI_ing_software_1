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
               ) -> Car:
        
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

    def get_brand(self, id:int) -> Brand:
        return Brand.objects.get(id=id)
    
    def get_category(self, id:int) -> Category:
        return Category.objects.get(id=id)

    def filter_many(self,
                    price_gte: int,
                    price_lte: int,
                    brand_id: int,
                    used: int,
                    category_id: int,
                    year_gte: int,
                    year_lte: int,) -> List[Car]:
        listado = Car.objects.all()
        if price_gte != 0:
            listado = listado.filter(price__gte=price_gte)
        if price_lte != 0:
            listado = listado.filter(price__lte=price_lte)
        if brand_id != 0:
            brand = self.get_brand(brand_id)
            listado = listado.filter(brand=brand)
        if used != 2:
            listado = listado.filter(used=used)
        if category_id != 0:
            category = self.get_category(category_id)
            listado = listado.filter(category=category)
        if year_gte != 0:
            listado = listado.filter(year__gte=year_gte)
        if year_lte != 0:
            listado = listado.filter(year__lte=year_lte)
        listado = listado.filter(sold=False)
        return listado

    def filter_by_category(
            self,
            category = Category,
    ) -> List[Car]:
        return category.objects.filter(category = category)

    def delete(self, car:Car):
        car.delete()
