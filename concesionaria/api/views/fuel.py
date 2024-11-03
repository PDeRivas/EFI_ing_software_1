from rest_framework.viewsets import ModelViewSet

from cars.repositories.car_components_repository import FuelRepository

from api.serializers.fuel_serializer import FuelSerializer

class FuelViewSet(ModelViewSet):
    repo = FuelRepository()
    queryset = repo.get_all()
    serializer_class = FuelSerializer
