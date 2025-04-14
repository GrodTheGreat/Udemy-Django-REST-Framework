from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.WatchListAV.as_view(), name="watch-list"),
    path(
        route="<int:pk>",
        view=views.WatchListDetailsAV.as_view(),
        name="watch-list-details",
    ),
    path(
        route="platforms/",
        view=views.StreamingPlatformListAV.as_view(),
        name="platform-list",
    ),
    path(
        route="platforms/<int:pk>/",
        view=views.StreamingPlatformDetailsAV.as_view(),
        name="platform-details",
    ),
    # Function-based Views
    # path(route="", view=views.movie_list, name='movie-list'),
    # path(route="<int:pk>", view=views.movie_details, name='movie-details'),
]
