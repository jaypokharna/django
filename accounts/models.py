from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

class CustomUser(AbstractUser):
    
    # username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    username = None
    phone_number = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=150)
    user_profile_image = models.ImageField(upload_to="profile_image")

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()