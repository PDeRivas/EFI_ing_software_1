from rest_framework import serializers

from cars.models import(
    Comment
)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'time')
