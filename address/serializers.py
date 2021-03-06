from rest_framework import serializers

from .models import Country, City, District, Address


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ("url", "name", "code", "slug")
        extra_kwargs = {"slug": {"read_only": True}}


class CitySerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.SlugRelatedField(
        queryset=Country.objects.all(), slug_field="name"
    )

    class Meta:
        model = City
        fields = ("url", "name", "country", "slug")
        extra_kwargs = {"slug": {"read_only": True}}


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.SlugRelatedField(queryset=City.objects.all(), slug_field="name")

    class Meta:
        model = District
        fields = ("url", "name", "city", "slug")
        extra_kwargs = {"slug": {"read_only": True}}


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    district = serializers.SlugRelatedField(
        queryset=District.objects.all(), slug_field="name"
    )

    class Meta:
        model = Address
        fields = ("address_line", "district", "raw")
        extra_kwargs = {"raw": {"read_only": True}}
