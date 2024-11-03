from rest_framework.viewsets import ModelViewSet

from cars.repositories.car_components_repository import CategoryRepository
from api.serializers.category_serializer import CategorySerializer

class CategoryViewSet(ModelViewSet):
    repo = CategoryRepository()
    queryset = repo.get_all()
    serializer_class = CategorySerializer
