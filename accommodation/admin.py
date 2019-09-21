from django.contrib import admin

from accommodation.models import (
    AccommodationType,
    Accommodation,
    Room,
    RoomType,
    Booking,
)

# Register your models here.
admin.site.register(AccommodationType)
admin.site.register(Accommodation)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Booking)
