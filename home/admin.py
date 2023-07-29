from django.contrib import admin
from .models import User, GymLocation, GymClass, Attendance, EquipmentFacilities, PaymentOption, Membership
from django_summernote.admin import SummernoteModelAdmin


@admin.register(PaymentOption)
class PaymentOption(SummernoteModelAdmin):

    list_display = ('Monthly',)


@admin.register(Membership)
class Membership(SummernoteModelAdmin):

    list_display = (
        'order_number', 'full_name', 'email', 'phone_number', 'date', 'subscription')


@admin.register(User)
class UserId(SummernoteModelAdmin):

    list_display = ('name', 'email', 'user_id')


@admin.register(GymLocation)
class LocationsAdmin(SummernoteModelAdmin):

    list_display = (
        'location', 'address', 'postcode', 'phone_number', 'equipment_facilities', 'classes')


@admin.register(GymClass)
class GymClasses(SummernoteModelAdmin):

    list_display = ('class_name', 'class_schedule')


@admin.register(Attendance)
class ClassAttendance(SummernoteModelAdmin):

    list_display = ('user', 'location', 'scheduled')


@admin.register(EquipmentFacilities)
class Equip_Facil(SummernoteModelAdmin):

    list_display = ('equipment_available',)
