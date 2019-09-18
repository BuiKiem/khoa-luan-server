from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """The Manager class used for the custom User class."""

    def create_user(self, email: str, password: str) -> "User":
        """
        Create and save a new user

        :param email: User email (required)
        :param password: User password (required)
        :return: created user
        """
        if not email:
            raise ValueError("User must have an email address.")
        if not password:
            raise ValueError("User must have a password.")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staff(self, email: str, password: str) -> "User":
        """
        Create and save a new staff-user

        :param email: staff-user's email
        :param password: staff-user's password
        :return: created staff-user
        """

        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = False
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str) -> "User":
        """
        Create and save a new superuser

        :param email: superuser's email
        :param password: superuser's password
        :return: created superuser
        """

        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
