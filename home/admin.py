from django.contrib import admin
from .models import GymLocation
from django_summernote.admin import SummernoteModelAdmin


@admin.register(GymLocation)
class LocationsAdmin(SummernoteModelAdmin):

    list_display = ('name', 'location', 'equipment')
