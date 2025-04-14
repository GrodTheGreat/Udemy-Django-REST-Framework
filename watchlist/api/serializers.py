from typing import Any, Mapping
from rest_framework import serializers

from ..models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data: Mapping[str, Any]) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(
        self,
        instance: Movie,
        validated_data: Mapping[str, Any],
    ) -> Movie:
        instance.name = validated_data.get(key="name", default=instance.name)
        instance.description = validated_data.get(
            key="description",
            default=instance.description,
        )
        instance.active = validated_data.get(
            key="active",
            default=instance.active,
        )
        instance.save()

        return instance
