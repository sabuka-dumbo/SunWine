from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=150, default="")
    phone_number = models.CharField(max_length=150, default="")

    def __str__(self):
        return f"{self.full_name}"

class Rooms(models.Model):
    room_number = models.IntegerField(default=1)
    room_title = models.CharField(max_length=1000, default='')
    available = models.BooleanField(default=True)
    price = models.IntegerField(default=1)
    bed = models.IntegerField(default=1)
    tv = models.IntegerField(default=1)
    storage = models.IntegerField(default=1)
    bathroom = models.IntegerField(default=1)
    balcony = models.IntegerField(default=1)
    mirror = models.IntegerField()
    fridge = models.IntegerField(default=1)
    desk = models.IntegerField(default=1)
    items = models.IntegerField(default=1)
    kvadratuloba = models.IntegerField(default=1)
    couche = models.IntegerField(default=1)
    image1 = models.ImageField(upload_to='pics/', default='', blank=True, null=True)
    image2 = models.ImageField(upload_to='pics/', default='', blank=True, null=True)
    image3 = models.ImageField(upload_to='pics/', default='', blank=True, null=True)
    image4 = models.ImageField(upload_to='pics/', default='', blank=True, null=True)
    description = models.CharField(max_length=2000, default='')


    def __str__(self):
        return f"{self.room_number}"
    
class Check_In(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', default='')
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='room', default='')
    persons = models.PositiveIntegerField(default=1)
    reserved = models.BooleanField(default=True)
    check_in = models.DateField(default=datetime.date.today)
    check_out = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"Room"

    
class Services(models.Model):
    service_title = models.CharField(max_length=300)
    service_description = models.CharField(max_length=800)
    service_image = models.ImageField(upload_to='pics/')

    def __str__(self):
        return f"{self.service_title}"
    
class Contact(models.Model):
    phone_number = models.IntegerField()
    email = models.EmailField()
    whatsapp = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return f"Contacts {self.pk}"
