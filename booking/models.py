from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('General Service','General Service'),
        ('Oil Change','Oil Change'),
        ('Engine Repair','Engine Repair'),
        ('Water Wash','Water Wash'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_no = models.CharField(max_length=50)
    service_type = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.vehicle_no}"
