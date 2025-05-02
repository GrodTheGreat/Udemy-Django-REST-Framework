from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import RegistrationSerializer


@api_view(http_method_names=["POST"])
def registration_view(request: Request) -> Response:
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data)
