from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
