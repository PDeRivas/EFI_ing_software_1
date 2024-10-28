from rest_framework.viewsets import ModelViewSet

from cars.models import Fuel
from api.serializers.fuel_serializer import FuelSerializer

class FuelViewSet(ModelViewSet):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer
