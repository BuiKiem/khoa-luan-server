from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from accommodation.models import (
    AccommodationType,
    Accommodation,
    RoomType,
    Room,
    Booking,
)
from accommodation.serializers import (
    AccommodationTypeSerializer,
    AccommodationSerializer,
    RoomTypeSerializer,
    RoomSerializer,
    BookingSerializer,
)
from address.models import City, District


class AccommodationTypeViewSet(viewsets.ModelViewSet):
    queryset = AccommodationType.objects.all()
    serializer_class = AccommodationTypeSerializer


class AccommodationViewSet(viewsets.ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer

    @action(methods=["GET"], detail=False, url_path="search")
    def search_accommodations(self, request: Request):
        location_type = request.query_params.get("location-type", "")
        location = request.query_params.get("location", "")
        selected_city = None
        selected_district = None

        if not all([location_type, location]):
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": "Not provide enough parameter"},
            )

        if location_type == "city":
            selected_city = get_object_or_404(City, pk=location)
        elif location_type == "district":
            selected_district = get_object_or_404(District, pk=location)

        hotels = Accommodation.objects.filter(
            Q(address__district=selected_district)
            | Q(address__district__city=selected_city)
        )
        serializer = self.get_serializer(hotels, many=True)

        return Response(serializer.data)


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
