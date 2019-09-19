from django.db import models
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=40, unique=True)
    code = models.CharField(max_length=2)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ("name",)

    def __str__(self):
        return "%s" % (self.name or self.code)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    country = models.ForeignKey(
        "Country", on_delete=models.CASCADE, related_name="cities", null=False
    )

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ("name",)

    def __str__(self):
        if self.country:
            return f"{self.name}, {self.country.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class District(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    city = models.ForeignKey(
        "City", on_delete=models.CASCADE, related_name="districts", null=False
    )

    class Meta:
        unique_together = (("name", "city"),)
        ordering = ("city__name", "name")

    def __str__(self):
        return f"{self.name}, {self.city.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}-{self.city.name}")
        super().save(*args, **kwargs)


class Address(models.Model):
    address_line = models.CharField(max_length=100)
    raw = models.CharField(max_length=200)

    district = models.ForeignKey(
        "District", related_name="addresses", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Adresses"
        ordering = ("district", "address_line")

    def __str__(self):
        return self.raw

    def save(self, *args, **kwargs):
        district = self.district.name
        city = self.district.city.name
        country = self.district.city.country.name
        self.raw = f"{self.address_line}, {district}, {city}, {country}"
        super().save(*args, *kwargs)
