from typing import Dict

from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile model"""

    class Meta:
        model = Profile
        fields = ("gender", "location", "birth_date")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the User model"""

    profile = ProfileSerializer()

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
