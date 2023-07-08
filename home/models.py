import uuid

from django.db import models
from django.contrib.auth.models import User


class PaymentOption(models.Model):
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    annual = models.BooleanField(default=False)
    monthly = models.BooleanField(default=False)
    day_pass = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'PaymentOption'


class Membership(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    subscription = models.ForeignKey(
        PaymentOption, on_delete=models.CASCADE, related_name="subscription", null=True)

    def generate_order_number(self):

        return uuid.uuid4().hex.upper()

    def __str__(self):

        return self.order_number

    class Meta:
        verbose_name_plural = 'Membership'


# class BuyMembership(models.Model):
#     membership = models.ForeignKey(
#         Membership, on_delete=models.CASCADE, related_name="BuyMembership")
#     subscription = models.ForeignKey(
#         PaymentOption, on_delete=models.CASCADE, related_name="subscription")
#     membership_total = models.DecimalField(
#         max_digits=6, decimal_places=2, null=False, blank=False, editable=False)


class User(models.Model):
    name = models.TextField(max_length=20, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    user_id = models.CharField(max_length=20, unique=True, null=True)
    # membership = models.ForeignKey(
    #     Membership, on_delete=models.CASCADE, related_name="Membership")

    class Meta:
        verbose_name_plural = 'User'


class GymClass(models.Model):
    class_name = models.CharField(max_length=20, unique=True)
    class_schedule = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name_plural = 'GymClass'


class EquipmentFacilities(models.Model):
    free_parking = models.CharField(max_length=20, null=True)
    changing_rooms = models.CharField(max_length=20, null=True)
    lockers = models.CharField(max_length=20, null=True)
    sunbeds = models.CharField(max_length=20, null=True)
    sauna = models.CharField(max_length=20, null=True)
    pool = models.CharField(max_length=20, null=True)
    personal_trainer = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name_plural = 'EquipmentFacilities'


class GymLocation(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    location = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100, unique=True)
    postcode = models.CharField(max_length=7, default=True, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    equipment_facilities = models.ForeignKey(
        'EquipmentFacilities', on_delete=models.CASCADE, default=True, related_name="equip_facil")
    classes = models.ForeignKey(
        'GymClass', on_delete=models.CASCADE, default=True, related_name="classes")
    class_schedule = models.ForeignKey(
        'GymClass', on_delete=models.CASCADE, default=True, related_name="schedule")

    class Meta:
        verbose_name_plural = 'GymLocation'


class Attendance(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user")
    location = models.ForeignKey(
        GymLocation, on_delete=models.CASCADE, related_name="class_location")
    scheduled = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Attendance'
