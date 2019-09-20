from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Address


@receiver(pre_save, sender=Address)
def modify_raw_field(sender: Address, instance: Address, **kwargs):
    address_line = instance.address_line
    district = instance.district.name
    city = instance.district.city.name
    country = instance.district.city.country.name

    instance.raw = f"{address_line}, {district}, {city}, {country}"
