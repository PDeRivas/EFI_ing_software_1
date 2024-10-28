from rest_framework import serializers

from cars.models import(
    Fuel
)

class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('name',)
