from django.db import models
from django.contrib.auth import get_user_model

from address.models import Address


class AccommodationType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Accommodation(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    accommodation_type = models.ForeignKey(
        AccommodationType, on_delete=models.CASCADE, related_name="accommodations"
    )
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, related_name="accommodation"
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class RoomType(models.Model):
    name = models.CharField(max_length=50)
    guest_capacity = models.SmallIntegerField()
    bed_number = models.SmallIntegerField()

    class Meta:
        ordering = ("guest_capacity", "bed_number", "name")

    def __str__(self):
        return f"{self.name} ({self.guest_capacity})({self.bed_number})"


class Room(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()

    room_type = models.ForeignKey(
        RoomType, on_delete=models.CASCADE, related_name="rooms"
    )
    accommodation = models.ForeignKey(
        Accommodation, on_delete=models.CASCADE, related_name="rooms"
    )

    class Meta:
        ordering = ("price",)

    def __str__(self):
        return f"{self.name} ({self.room_type.name}) - {self.price}"


class Booking(models.Model):
    PENDING = "PENDING"
    PAID = "PAID"
    CANCELLED = "CANCELLED"
    OVERDUE = "OVERDUE"
    REFUNDED = "REFUNDED"
    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (PAID, "Paid"),
        (CANCELLED, "Cancelled"),
        (OVERDUE, "Overdue"),
        (REFUNDED, "Refunded"),
    )

    room_quantity = models.SmallIntegerField()
    guest_quantity = models.SmallIntegerField()
    additional_request = models.TextField()
    booking_date = models.DateField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

    room = models.ForeignKey(Room, related_name="bookings", on_delete=models.CASCADE)
    accommodation = models.ForeignKey(
        Accommodation, related_name="bookings", on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        get_user_model(), related_name="bookings", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-booking_date",)

    def __str__(self):
        return f"{self.accommodation.name} - {self.owner.name} ({self.get_status_display()})"
