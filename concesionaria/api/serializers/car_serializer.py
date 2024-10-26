from rest_framework import serializers

from cars.models import(
    Car
)

from api.serializers.brand_serializer import BrandSerializer
from api.serializers.nameplate_serializer import NameplateSerializer

class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    nameplate = NameplateSerializer()
    class Meta:
        model = Car
        fields = '__all__'