from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["options", "get", "post", "put", "patch"]

    @action(detail=True, methods=["GET"], serializer_class=ProfileSerializer)
    def profile(self, request: Request, pk: int = None):
        try:
            profile = self.get_object().profile
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @profile.mapping.patch
    def update_profile_partial(self, request: Request, pk: int = None):
        try:
            profile = self.get_object().profile
            serializer = ProfileSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
