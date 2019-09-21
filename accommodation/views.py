from rest_framework import viewsets

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


class AccommodationTypeViewSet(viewsets.ModelViewSet):
    queryset = AccommodationType.objects.all()
    serializer_class = AccommodationTypeSerializer


class AccommodationViewSet(viewsets.ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
