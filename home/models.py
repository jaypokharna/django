from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.TextField()
    address = models.TextField(null=True , blank=True)
    

class Car(models.Model):
    cname = models.CharField(max_length=50)
    speed=models.IntegerField(default=50)

    def __str__(self) -> int:
        return self.cname