from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    guests_count = models.IntegerField()
    booking_date = models.DateTimeField()
    
class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()