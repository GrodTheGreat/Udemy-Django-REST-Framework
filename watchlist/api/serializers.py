# from typing import Any, Mapping
from rest_framework import serializers

from ..models import Review, StreamingPlatform, WatchList


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ["watchlist"]


class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = [
            "id",
            "title",
            "storyline",
            "platform",
            "active",
            "created",
            "reviews",
            # "len_name",
        ]  # or "__all__"
        # exclude = ['active']

    # def get_len_name(self, object: WatchList) -> int:
    #     return len(object.title)

    # def validate_name(self, value: str) -> str:
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")

    #     return value

    # def validate(self, data: Mapping[str, Any]) -> Mapping[str, Any]:
    #     if data["name"] == data["description"]:
    #         raise serializers.ValidationError(
    #             "Name and Description must be different!"
    #         )

    #     return data


class StreamingPlatformSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="platform-details", lookup_field="pk"
    )
    #! Name must match model field
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="watch-list-details",
        lookup_field="pk",
    )
    # watchlist = serializers.StringRelatedField(many=True, read_only=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="watch-list-details",
    # )

    class Meta:
        model = StreamingPlatform
        fields = ["url", "id", "watchlist", "name", "about", "website"]


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
