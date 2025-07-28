from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=150, default="")
    phone_number = models.CharField(max_length=150, default="")

    def __str__(self):
        return f"მომხმარებელი: {self.full_name}"

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
        return f"ოთახის ნომერი: {self.room_number}"
    
class Check_In(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', default='')
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='room', default='')
    persons = models.CharField(default='', max_length=150)
    reserved = models.BooleanField(default=True)
    check_in = models.DateField(default=datetime.date.today)
    check_out = models.DateField(default=datetime.date.today)
    comment = models.CharField(default='', max_length=1000)

    def __str__(self):
        return f"ჩექ-ინი ოთახ {self.room.room_number}, {self.check_in}-დან {self.check_out}-მდე."

    
class Services(models.Model):
    service_title = models.CharField(max_length=300)
    service_description = models.CharField(max_length=800)
    service_image = models.ImageField(upload_to='pics/')

    def __str__(self):
        return f"სერვისი: {self.service_title}"
    
class Contact(models.Model):
    phone_number = models.IntegerField()
    email = models.EmailField()
    whatsapp = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return f"საკონტაქტო {self.pk}"

class Gallery(models.Model):
    image1 = models.ImageField(upload_to='pics/')
    image2 = models.ImageField(upload_to='pics/')
    image3 = models.ImageField(upload_to='pics/')
    image4 = models.ImageField(upload_to='pics/')
    image5 = models.ImageField(upload_to='pics/')
    image6 = models.ImageField(upload_to='pics/')
    image7 = models.ImageField(upload_to='pics/')
    image8 = models.ImageField(upload_to='pics/')

    def __str__(self):
        return f"გალერეა {self.pk}"

class Indexpage(models.Model):
    title1 = models.CharField(max_length=1500, default='')
    title2 = models.CharField(max_length=1500, default='')
    title3 = models.CharField(max_length=1500, default='')
    title4 = models.CharField(max_length=1500, default='')
    title5 = models.CharField(max_length=1500, default='')
    title6 = models.CharField(max_length=1500, default='')
    title7= models.CharField(max_length=1500, default='')
    title8 = models.CharField(max_length=1500, default='')
    title9 = models.CharField(max_length=1500, default='')
    title10 = models.CharField(max_length=1500, default='')
    title11 = models.CharField(max_length=1500, default='')
    title12 = models.CharField(max_length=1500, default='')
    image1 = models.ImageField(default='')
    image2 = models.ImageField(default='')
    image3 = models.ImageField(default='')
    image4 = models.ImageField(default='')
    image5 = models.ImageField(default='')

    def __str__(self):
        return f"ინფორმაციის გვერდის ინფორმაცია"