from rest_framework.routers import DefaultRouter

from api.views.car import CarViewSet
from api.views.brand import BrandViewSet
from api.views.nameplate import NameplateViewSet

router = DefaultRouter()

router.register(r'cars', CarViewSet, 'cars')
router.register(r'brands', BrandViewSet, 'brands')
router.register(r'nameplates', NameplateViewSet, 'nameplates')

urlpatterns = router.urls