from django.http import HttpRequest, JsonResponse

from .models import Movie


def movie_list(request: HttpRequest) -> JsonResponse:
    movies = Movie.objects.all()
    data = {"movies": list(movies.values())}

    return JsonResponse(data=data)


def movie_details(request: HttpRequest, pk: int) -> JsonResponse:
    movie = Movie.objects.get(pk=pk)
    data = {
        "name": movie.name,
        "description": movie.description,
        "active": movie.active,
    }

    return JsonResponse(data=data)
