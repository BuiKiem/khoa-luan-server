from django.contrib import admin

from .models import Country, City, District, Address

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Address)
