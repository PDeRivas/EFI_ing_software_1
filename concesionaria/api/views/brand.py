from rest_framework.viewsets import ModelViewSet

from cars.models import Brand
from api.serializers.brand_serializer import BrandSerializer

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
