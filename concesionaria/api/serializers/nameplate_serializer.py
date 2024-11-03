from rest_framework import serializers

from cars.models import(
    Nameplate
)

class NameplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nameplate
        fields = ('id', 'name',)
