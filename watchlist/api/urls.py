from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.MovieListAV.as_view(), name="movie-list"),
    path(
        route="<int:pk>",
        view=views.MovieDetailsAV.as_view(),
        name="movie-details",
    ),
    # Function-based Views
    # path(route="", view=views.movie_list, name='movie-list'),
    # path(route="<int:pk>", view=views.movie_details, name='movie-details'),
]
