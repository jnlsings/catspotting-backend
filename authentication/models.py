from django.db import models
from django.contrib.auth.models import AbstractUser

# Create custom user model


class CustomUser(AbstractUser):
    img_url = models.TextField()