from rest_framework.viewsets import ModelViewSet

from cars.models import Transmission
from api.serializers.transmission_serializer import TransmissionSerializer

class TransmissionViewSet(ModelViewSet):
    queryset = Transmission.objects.all()
    serializer_class = TransmissionSerializer
