from typing import (
    List,
    Optional,
)

from cars.models import(
    Car,
    Brand,
    Category,
    Comment,
    Fuel,
    Nameplate,
    Traction,
    Transmission,
)

#logger = logging.getLogger(__name__)

class BrandRepository:
    def get_all(self):
        return Brand.objects.all()
    
class CategoryRepository:
    def get_all(self):
        return Category.objects.all()

class CommentRepository:
    def get_all(self):
        return Comment.objects.all()    
    
class FuelRepository:
    def get_all(self):
        return Fuel.objects.all()
    
class NameplateRepository:
    def get_all(self):
        return Nameplate.objects.all()
    
class TractionRepository:
    def get_all(self):
        return Traction.objects.all()

class TransmissionRepository:
    def get_all(self):
        return Transmission.objects.all()