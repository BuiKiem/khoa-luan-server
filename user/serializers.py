from typing import Dict

from django.contrib.auth import get_user_model
from rest_framework import serializers

from address.models import Address
from address.serializers import AddressSerializer
from user.models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile model"""

    address = AddressSerializer(allow_null=True)

    class Meta:
        model = Profile
        fields = ("gender", "birth_date", "address")

    def create(self, validated_data):
        address_data = validated_data.pop("address", None)
        profile = Profile.objects.create(**validated_data)
        if address_data:
            Address.objects.create(user_profile=profile, **address_data)

    def update(self, instance, validated_data):
        address_data = validated_data.pop("address", None)
        address = instance.address

        if address_data and address:
            address.address_line = address_data.get(
                "address_line", address.address_line
            )
            address.district = address_data.get("district", address.district)
            address.save()
        elif address_data:
            address = Address.objects.create(**address_data)
            instance.address = address

        instance.gender = validated_data.get("gender", instance.gender)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.save()

        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the User model"""

    profile = serializers.HyperlinkedIdentityField(view_name="user-profile")

    class Meta:
        model = get_user_model()
        fields = ("url", "email", "password", "profile")
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: Dict):
        """Update the user, setting the password correctly and return it."""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
