from django.contrib import admin
from .models import GymLocation
from django_summernote.admin import SummernoteModelAdmin


@admin.register(GymLocation)
class LocationsAdmin(SummernoteModelAdmin):

    list_display = (
        'location', 'address', 'phone_number', 'equipment', 'gym_num')
    # list_filter = ('equipment', 'gym_num')
