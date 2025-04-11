from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response

from watchlist.api.serializers import MovieSerializer
from watchlist.models import Movie


@api_view()
def movie_list(request: HttpRequest) -> Response:
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)

    return Response(data=serializer.data)


@api_view()
def movie_details(request: HttpRequest, pk: int) -> Response:
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)

    return Response(data=serializer.data)
