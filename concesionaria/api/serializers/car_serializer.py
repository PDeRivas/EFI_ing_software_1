from rest_framework import serializers

from cars.models import(
    Car,
    Country
)

from api.serializers.brand_serializer import BrandSerializer
from api.serializers.category_serializer import CategorySerializer
from api.serializers.fuel_serializer import FuelSerializer
from api.serializers.nameplate_serializer import NameplateSerializer
from api.serializers.traction_serializer import TractionSerializer
from api.serializers.transmission_serializer import TransmissionSerializer

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)

class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    country = CountrySerializer()
    fuel = FuelSerializer()
    nameplate = NameplateSerializer()
    traction = TractionSerializer()
    transmission = TransmissionSerializer()
    
    class Meta:
        model = Car
        fields = ('id', 'year', 'brand', 'category', 'country', 'fuel', 'nameplate', 'traction', 'transmission', 'used', 'km', 'cylinders', 'price', 'sold')