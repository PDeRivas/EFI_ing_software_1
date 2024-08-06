from django.core.cache import cache
from django.db.models.functions import Concat
from cars.models import Car, CarImage

def all_car_names(request):
    car_names = cache.get('car_names')
    if car_names == None:
        car_names = Car.objects.annotate(name=Concat('brand', 'nameplate', 'year'))
        cache.set('car_names', car_names, 36000)
    return {'car_names': car_names}
