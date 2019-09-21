from rest_framework import serializers

from accommodation.models import (
    AccommodationType,
    Accommodation,
    Room,
    RoomType,
    Booking,
)


class AccommodationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccommodationType
        fields = ("url", "name")


class AccommodationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accommodation
        fields = (
            "url",
            "name",
            "phone",
            "description",
            "is_active",
            "accommodation_type",
            "address",
        )


class RoomTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomType
        fields = ("url", "name", "guest_capacity", "bed_number")


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ("url", "name", "price", "description", "room_type", "accommodation")


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "room_quantity",
            "guest_quantity",
            "additional_request",
            "booking_date",
            "checkin_date",
            "checkout_date",
            "status",
            "room",
            "accommodation",
            "owner",
        )
