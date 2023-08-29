from django.db import models

# Create your models here.
class Signup(models.Model):
    fullname = models.TextField()
    email = models.TextField()
    phnumber = models.IntegerField()
    password = models.TextField()