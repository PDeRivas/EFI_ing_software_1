from rest_framework import serializers

from cars.models import(
    Traction
)

class TractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traction
        fields = ('id', 'name',)
