from rest_framework.viewsets import ModelViewSet

from cars.repositories.car_repository import CarsRepository
from api.serializers.car_serializer import CarSerializer

class CarViewSet(ModelViewSet):
    repo = CarsRepository()
    queryset = repo.get_all()
    serializer_class = CarSerializer
