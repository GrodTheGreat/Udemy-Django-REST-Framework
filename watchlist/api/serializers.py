from typing import Any, Mapping
from rest_framework import serializers

from ..models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "name", "description", "active"]  # or "__all__"
        # exclude = ['active']

    def validate_name(self, value: str) -> str:
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")

        return value

    def validate(self, data: Mapping[str, Any]) -> Mapping[str, Any]:
        if data["name"] == data["description"]:
            raise serializers.ValidationError(
                "Name and Description must be different!"
            )

        return data


# * Basic Serializer
# def name_length(value: str) -> str:
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")

#     return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data: Mapping[str, Any]) -> Movie:
#         return Movie.objects.create(**validated_data)

#     def update(
#         self,
#         instance: Movie,
#         validated_data: Mapping[str, Any],
#     ) -> Movie:
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get(
#             "description",
#             instance.description,
#         )
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()

#         return instance

#     # You might be able to use Validators for this instead
#     # def validate_name(self, value: str) -> str:
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short!")

#     #     return value

#     def validate(self, data: Mapping[str, Any]) -> Mapping[str, Any]:
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError(
#                 "Name and Description must be different!"
#             )

#         return data
