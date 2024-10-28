from rest_framework import serializers

from cars.models import(
    Brand
)

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name',)
