from rest_framework.viewsets import ModelViewSet

from cars.models import Nameplate
from api.serializers.nameplate_serializer import NameplateSerializer

class NameplateViewSet(ModelViewSet):
    queryset = Nameplate.objects.all()
    serializer_class = NameplateSerializer