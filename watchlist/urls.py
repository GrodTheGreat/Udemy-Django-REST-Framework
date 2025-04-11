from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.movie_list),
    path(route="<int:pk>", view=views.movie_details),
]
