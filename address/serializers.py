from rest_framework import serializers

from .models import Country, City, District


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name", "code", "slug")
        extra_kwargs = {"slug": {"read_only": True}}


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("name", "country__name", "slug")
        extra_kwargs = {"slug": {"read_only": True}}


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ("name", "city__name", "slug")
        extra_kwargs = {"slug": {"read_only": True}}
