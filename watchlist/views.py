from django.http import HttpRequest, JsonResponse

from .models import Movie


def movie_list(request: HttpRequest) -> JsonResponse:
    movies = Movie.objects.all()
    data = {"movies": list(movies.values())}

    return JsonResponse(data=data)
