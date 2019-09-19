from django.db import models
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=40, unique=True)
    code = models.CharField(max_length=2)
    url = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ("name",)

    def __str__(self):
        return "%s" % (self.name or self.code)

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super().save(*args, **kwargs)


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.SlugField(unique=True)

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
        self.url = slugify(self.name)
        super().save(*args, **kwargs)


class District(models.Model):
    name = models.CharField(max_length=50)
    url = models.SlugField(unique=True)

    city = models.ForeignKey(
        "City", on_delete=models.CASCADE, related_name="districts", null=False
    )

    class Meta:
        unique_together = (("name", "city"),)
        ordering = ("city__name", "name")

    def __str__(self):
        return f"{self.name}, {self.city.name}"

    def save(self, *args, **kwargs):
        self.url = slugify(f"{self.name}-{self.id}")
        super().save(*args, **kwargs)
