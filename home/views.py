from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import GymLocation


def index(request):
    """ returns index page """
    return render(request, "home/index.html")


def LocationsView(request):
    """ returns gym locations page"""
    locations = GymLocation.objects.all()
    context = {
        'locations': locations,
    }
    return render(request, "home/locations.html", context)


def locations_detail(request):
    """ returns specific gym location page"""
    model = GymLocation
    
    return render(request, "home/locations_detail.html")


# class LoactionsDetail(View):
#     """ returns specific gym on individual page """
#     return render(request, "home/locations_detail.html")


def FAQs(request):
    """ returns gym locations page"""
    return render(request, "home/FAQs.html")
