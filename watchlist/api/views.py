from rest_framework import (
    generics,
    # mixins,
    status,
)

# from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist.api.serializers import (
    ReviewSerializer,
    StreamingPlatformSerializer,
    WatchListSerializer,
)
from watchlist.models import Review, StreamingPlatform, WatchList


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer: ReviewSerializer):
        pk = self.kwargs.get("pk")
        watchlist = WatchList.objects.get(pk=pk)

        serializer.save(watchlist=watchlist)


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# class ReviewList(generics.ListCreateAPIView):
class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)


# class ReviewDetails(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request: Request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request: Request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request: Request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class StreamingPlatformListAV(APIView):
    def get(self, request: Request) -> Response:
        streaming_platforms = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(
            streaming_platforms,
            many=True,
            context={"request": request},
        )

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = StreamingPlatformSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED,
        )


class StreamingPlatformDetailsAV(APIView):
    def get(self, request: Request, pk: int) -> Response:
        try:
            streaming_platform = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response(
                data={"Error": "Streaming Platform not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = StreamingPlatformSerializer(
            streaming_platform,
            context={"request": request},
        )

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request: Request, pk: int) -> Response:
        try:
            streaming_platform = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response(
                data={"Error": "Streaming Platform not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = StreamingPlatformSerializer(
            streaming_platform,
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request: Request, pk: int) -> Response:
        try:
            streaming_platform = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response(
                data={"Error": "Streaming Platform not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        streaming_platform.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):
    def get(self, request: Request) -> Response:
        watch_list = WatchList.objects.all()
        serializer = WatchListSerializer(watch_list, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class WatchListDetailsAV(APIView):
    def get(self, request: Request, pk: int) -> Response:
        try:
            watch_list = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                data={"Error": "Watch List not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = WatchListSerializer(watch_list)

        return Response(data=serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        try:
            watch_list = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                data={"Error": "Watch List not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = WatchListSerializer(watch_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request: Request, pk: int) -> Response:
        try:
            watch_list = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                data={"Error": "Watch List not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        watch_list.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# * Function-based Views
# @api_view(http_method_names=["GET", "POST"])
# def movie_list(request: Request) -> Response:
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)

#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST,
#             )


# @api_view(http_method_names=["GET", "PUT", "DELETE"])
# def movie_details(request: Request, pk: int) -> Response:
#     if request.method == "GET":
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 data={"Error": "Movie not found"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         serializer = MovieSerializer(movie)

#         return Response(data=serializer.data)

#     if request.method == "PUT":
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 data={"Error": "Movie not found"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#     if request.method == "DELETE":
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 data={"Error": "Movie not found"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         movie.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
