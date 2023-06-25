from django.db import models
from django.contrib.auth.models import User


# class GymClass():
#     className = models.TextField()
#     classSchedule = models.DateTimeField()
#     classLocation = models.ForeignKey(GymLocation,)


class GymLocation(models.Model):
    name = models.TextField(max_length=20)
    location = models.CharField(max_length=100)
    equipment = []
    # classes = models.ForeignKey(GymClass)


# class PaymentOption():
#     name = models.TextField()
#     length = models.DateField()
