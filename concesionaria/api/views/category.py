from rest_framework.viewsets import ModelViewSet

from cars.models import Category
from api.serializers.category_serializer import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
