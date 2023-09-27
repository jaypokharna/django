from django.db import models
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
# Create your models here.

class Car(models.Model):
    cname = models.CharField(max_length=50)
    speed=models.IntegerField(default=50)

    def __str__(self) -> int:
        return self.cname
    
    # class Meta:
    #     ordering = ['cname']
    
@receiver(pre_save , sender = Car)
def call_car_api(sender , instance , **kwargs):

    print("CAR OBJECT CREATED")
    print(f"Sender - {sender} \nInstance - {instance} \nKwargs - {kwargs}")
