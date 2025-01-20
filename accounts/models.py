# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Customized User Profile Model."""
    age = models.PositiveIntegerField(null=True, blank=True)
