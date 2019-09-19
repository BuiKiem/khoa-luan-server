from rest_framework import serializers

from .models import Country, City, District


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name", "code", "slug")
        extra_kwargs = {"slug": {"read_only": True}}


class CitySerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(
        queryset=Country.objects.all(), slug_field="name"
    )

    class Meta:
        model = City
        fields = ("name", "country", "slug")
        extra_kwargs = {"slug": {"read_only": True}}


class DistrictSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(queryset=City.objects.all(), slug_field="name")

    class Meta:
        model = District
        fields = ("name", "city", "slug")
        extra_kwargs = {"slug": {"read_only": True}}
