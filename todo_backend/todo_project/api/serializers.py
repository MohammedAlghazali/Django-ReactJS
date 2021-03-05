from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=80)
    description = serializers.CharField(max_length=400)

    def create(self, validated_data):
        return Todo.object.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
