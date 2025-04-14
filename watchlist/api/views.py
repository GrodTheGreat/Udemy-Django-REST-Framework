from django.http import HttpRequest
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

        return Response(data=serializer.data)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(http_method_names=["GET", "PUT", "DELETE"])
def movie_details(request: HttpRequest | Request, pk: int) -> Response:
    if request.method == "GET":
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)

        return Response(data=serializer.data)

    if request.method == "PUT":
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == "DELETE":
        movie = Movie.objects.get(pk=pk)
        movie.delete()

        return Response()
