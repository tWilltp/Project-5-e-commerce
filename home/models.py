from django.db import models
from django.contrib.auth.models import User


class PaymentOption(models.Model):
    annual = int()
    monthly = int()
    day_pass = int()


class User(models.Model):
    name = models.TextField(max_length=20, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    user_id = models.CharField(max_length=20, unique=True)
    payment_option = models.ForeignKey(
        PaymentOption, on_delete=models.CASCADE, related_name="subscription")


class GymClass(models.Model):
    class_name = models.TextField(max_length=20, unique=True)
    class_schedule = models.DateTimeField(auto_now_add=True)


class EquipmentFacilities(models.Model):
    free_parking = models.BooleanField()
    changing_rooms = models.BooleanField()
    lockers = models.BooleanField()
    sunbeds = models.BooleanField()
    sauna = models.BooleanField()
    pool = models.BooleanField()
    personal_trainer = models.BooleanField()


class GymLocation(models.Model):
    location = models.TextField(max_length=20, unique=True)
    address = models.CharField(max_length=100, unique=True)
    postcode = models.CharField(max_length=7, default=True, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    equipment_facilities = models.ForeignKey(
        'EquipmentFacilities', on_delete=models.CASCADE, default=True, related_name="equip_facil")
    classes = models.ForeignKey(
        'GymClass', on_delete=models.CASCADE, default=True, related_name="classes")


class Attendance(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user")
    location = models.ForeignKey(
        GymLocation, on_delete=models.CASCADE, related_name="class_location")
    scheduled = models.DateTimeField(auto_now_add=True)
