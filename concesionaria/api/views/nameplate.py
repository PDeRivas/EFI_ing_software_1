from rest_framework.viewsets import ModelViewSet

from cars.repositories.car_components_repository import NameplateRepository

from api.serializers.nameplate_serializer import NameplateSerializer

class NameplateViewSet(ModelViewSet):
    repo = NameplateRepository()
    queryset = repo.get_all()
    serializer_class = NameplateSerializer
