from django.db import models

# Create your models here.
from django.db import models

class Menu(models.Model):
    id = models.IntegerField(max_length=5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(max_length=5)

    def __str__(self):
        return self.name

class Booking(models.Model):
    id = models.IntegerField(max_length=11)
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField(max_length=6)
    bookingDate = models.DateTimeField

    def __str__(self):
        return f"{self.customer_name} - {self.date} at {self.time}"