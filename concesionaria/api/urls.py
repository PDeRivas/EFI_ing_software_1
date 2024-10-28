from rest_framework.routers import DefaultRouter

from api.views.car import CarViewSet
from api.views.brand import BrandViewSet
from api.views.category import CategoryViewSet
from api.views.fuel import FuelViewSet
from api.views.nameplate import NameplateViewSet
from api.views.traction import TractionViewSet
from api.views.transmission import TransmissionViewSet

router = DefaultRouter()

router.register(r'cars', CarViewSet, 'cars')
router.register(r'brands', BrandViewSet, 'brands')
router.register(r'category', CategoryViewSet, 'category')
router.register(r'nameplates', NameplateViewSet, 'nameplates')
router.register(r'fuel', FuelViewSet, 'fuel')
router.register(r'traction', TractionViewSet, 'traction')
router.register(r'transmission', TransmissionViewSet, 'Transmission')

urlpatterns = router.urls
