from django.db import models
from django.utils import timezone

class Booking(models.Model):
    user = models.CharField(max_length=200,null=True)
    date = models.DateField()
    booked = models.BooleanField(default=False)
    phonenumber = models.CharField(max_length=15,null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.user} - {self.date}"
