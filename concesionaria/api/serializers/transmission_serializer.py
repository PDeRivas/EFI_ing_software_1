from rest_framework import serializers

from cars.models import(
    Transmission
)

class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = ('name',)
