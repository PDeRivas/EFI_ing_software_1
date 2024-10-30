from django.core.cache import cache
from django.db.models.functions import Concat
from cars.models import Car, CarImage
from users.models import Profile

def all_car_names(request):
    car_names = cache.get('car_names')
    if car_names == None:
        cars = Car.objects.filter(sold=False)
        car_names = cars.annotate(name=Concat('brand', 'nameplate', 'year'))
        cache.set('car_names', car_names, 120)
    return {'car_names': car_names}

def profile(request):
    try:
        profile = Profile.objects.get(user=request.user.id)
    # Si no hay usuario retornara None
    except:
        profile = None
    finally:
        return {
            'profile': profile
        }
