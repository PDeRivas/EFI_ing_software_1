from rest_framework.viewsets import ModelViewSet

from cars.models import Traction
from api.serializers.traction_serializer import TractionSerializer

class TractionViewSet(ModelViewSet):
    queryset = Traction.objects.all()
    serializer_class = TractionSerializer
