from django.http import HttpRequest, JsonResponse

from .models import WatchList


def movie_list(request: HttpRequest) -> JsonResponse:
    movies = WatchList.objects.all()
    data = {"movies": list(movies.values())}

    return JsonResponse(data=data)


def movie_details(request: HttpRequest, pk: int) -> JsonResponse:
    movie = WatchList.objects.get(pk=pk)
    data = {
        "name": movie.title,
        "description": movie.storyline,
        "active": movie.active,
    }

    return JsonResponse(data=data)
