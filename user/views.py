from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    def list(self, request: Request) -> Response:
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request: Request, pk: int = None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user, context={"request": request})
        return Response(serializer.data)
