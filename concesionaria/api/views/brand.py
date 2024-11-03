from rest_framework.viewsets import ModelViewSet

from cars.repositories.car_components_repository import BrandRepository
from api.serializers.brand_serializer import BrandSerializer

class BrandViewSet(ModelViewSet):
    repo = BrandRepository()
    queryset = repo.get_all()
    serializer_class = BrandSerializer
