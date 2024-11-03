from rest_framework.viewsets import ModelViewSet

from cars.repositories.car_components_repository import TractionRepository

from api.serializers.traction_serializer import TractionSerializer

class TractionViewSet(ModelViewSet):
    repo = TractionRepository()
    queryset = repo.get_all()
    serializer_class = TractionSerializer
