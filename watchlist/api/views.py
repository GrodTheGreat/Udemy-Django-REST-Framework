from django.http import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from watchlist.api.serializers import MovieSerializer
from watchlist.models import Movie


@api_view(http_method_names=["GET", "POST"])
def movie_list(request: HttpRequest | Request) -> Response:
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


@api_view(http_method_names=["GET", "PUT", "DELETE"])
def movie_details(request: HttpRequest | Request, pk: int) -> Response:
    if request.method == "GET":
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                data={"Error": "Movie not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = MovieSerializer(movie)

        return Response(data=serializer.data)

    if request.method == "PUT":
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                data={"Error": "Movie not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    if request.method == "DELETE":
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                data={"Error": "Movie not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
