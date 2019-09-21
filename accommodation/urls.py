from rest_framework import routers

from accommodation.views import (
    AccommodationTypeViewSet,
    AccommodationViewSet,
    RoomTypeViewSet,
    RoomViewSet,
    BookingViewSet,
)


accommodation_router = routers.DefaultRouter()
accommodation_router.register(
    r"accommodation-types", AccommodationTypeViewSet, basename="accommodationtype"
)
accommodation_router.register(
    r"accommodations", AccommodationViewSet, basename="accommodation"
)
accommodation_router.register(r"room-types", RoomTypeViewSet, basename="room-type")
accommodation_router.register(r"rooms", RoomViewSet, basename="room")
accommodation_router.register(r"bookings", BookingViewSet, basename="booking")
