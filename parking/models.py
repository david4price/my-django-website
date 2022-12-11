from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50, null=True)
    # username = models.CharField(max_length=20, unique=True, null=True)
    email = models.EmailField(unique=True, null=True)
    car_num = models.CharField(unique=False, null=True, max_length=10)
    avater = models.ImageField(null=True, default="avatar.svg")
    balance = models.FloatField(null=True, default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"


class LotType(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name


class ParkingLot(models.Model):
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lot_type = models.ForeignKey(LotType, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    users = models.ManyToManyField(User, related_name='users', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class ParkingTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parkingLot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    ticket = models.IntegerField(null=True)
    enter_time = models.DateTimeField(auto_now_add=True)
    enter_time2 = models.CharField(null=True, max_length=20)
    exit_time = models.CharField(null=True, max_length=20)

    def __str__(self):
        return f"{self.ticket}, {self.enter_time}, {self.exit_time}"
