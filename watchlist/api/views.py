from rest_framework import status

# from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist.api.serializers import MovieSerializer
from watchlist.models import Movie


class MovieListAV(APIView):
    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class MovieDetailsAV(APIView):
    def get(self, request: Request, pk: int) -> Response:
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                data={"Error": "Movie not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = MovieSerializer(movie)

        return Response(data=serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                data={"Error": "Movie not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = MovieSerializer(movie, data=request.data)
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
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                data={"Error": "Movie not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        movie.delete()

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
