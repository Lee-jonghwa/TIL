from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')