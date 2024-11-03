from rest_framework.viewsets import ModelViewSet

from cars.repositories.car_components_repository import TransmissionRepository

from api.serializers.transmission_serializer import TransmissionSerializer

class TransmissionViewSet(ModelViewSet):
    repo = TransmissionRepository()
    queryset = repo.get_all()
    serializer_class = TransmissionSerializer
