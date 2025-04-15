from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(
    prefix="platforms",
    viewset=views.StreamingPlatformViewSet,
    basename="platform",
)

urlpatterns = [
    path(route="", view=views.WatchListAV.as_view(), name="watch-list"),
    path(
        route="<int:pk>",
        view=views.WatchListDetailsAV.as_view(),
        name="watch-list-details",
    ),
    # path(
    #     route="<int:pk>/reviews/",
    #     view=views.ReviewList.as_view(),
    #     name="review-list",
    # ),
    # path(
    #     route="reviews/<int:pk>",
    #     view=views.ReviewDetails.as_view(),
    #     name="review-details",
    # ),
    # path(route="reviews/", view=views.ReviewList.as_view(), name="reviews"),
    # path(
    #     route="reviews/<int:pk>/",
    #     view=views.ReviewDetails.as_view(),
    #     name="reviews",
    # ),
    path(
        route="<int:pk>/reviews/",
        view=views.ReviewList.as_view(),
        name="review-list",
    ),
    path(
        route="<int:pk>/reviews-create",
        view=views.ReviewCreate.as_view(),
        name="review-create",
    ),
    path(
        route="reviews/<int:pk>",
        view=views.ReviewDetails.as_view(),
        name="review-details",
    ),
    # path(
    #     route="platforms/",
    #     view=views.StreamingPlatformListAV.as_view(),
    #     name="platform-list",
    # ),
    # path(
    #     route="platforms/<int:pk>",
    #     view=views.StreamingPlatformDetailsAV.as_view(),
    #     name="platform-details",
    # ),
    path(route="", view=include(router.urls)),
    # Function-based Views
    # path(route="", view=views.movie_list, name='movie-list'),
    # path(route="<int:pk>", view=views.movie_details, name='movie-details'),
]
