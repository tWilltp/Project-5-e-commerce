from django.db import models
from django.contrib.auth.models import User


# class User():
#     name = blank
#     payment_option = blank


class GymLocation(models.Model):
    location = models.TextField(max_length=20)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=7)
    phone_number = models.CharField(max_length=11)
    equipment = []
    # classes = models.ForeignKey(GymClass)


# class GymClass():
#     className = models.TextField()
#     classSchedule = models.DateTimeField()
#     classLocation = models.ForeignKey(GymLocation, on_delete=models.CASCADE)


# class Attendance():
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     location = models.ForeignKey(GymLocation, on_delete=models.CASCADE)
#     scheduled = models.DateTimeField()
#     available = int(), max_space, STATUS=1/0, is_user_authenticated


# class Equipment():
#     spa = true/false
#     var = true/false
#     otr = true/false
#     itm = true/false
#     location = for_equipment


# class PaymentOption():
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     annual = int()
#     monthly = int()
#     day_pass = int()
