from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import GymLocation


def index(request):
    """ returns index page """
    return render(request, "home/index.html")


class LocationsView(View):
    """ returns gym locations page"""
    model = GymLocation
    template_name = 'locations.html'


def locations_detail(request):
    """ returns specific gym on individual page """
    return render(request, "home/locations_detail.html")


class LoactionsDetail(View):
    pass


def FAQs(request):
    """ returns gym locations page"""
    return render(request, "home/FAQs.html")
