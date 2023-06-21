from django.shortcuts import render


def index(request):
    """ returns index page """
    return render(request, "home/index.html")


def locations(request):
    """ returns gym locations page"""
    return render(request, "home/locations.html")


def FAQs(request):
    """ returns gym locations page"""
    return render(request, "home/FAQs.html")
