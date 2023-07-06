from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import GymLocation
from .forms import MembershipForm


def index(request):
    """ returns index page """
    return render(request, "home/index.html")


def LocationsView(request):
    """ returns gym locations page"""
    location = GymLocation.objects.all()
    context = {
        'location': location,
    }
    return render(request, "home/locations.html", context)


class locations_detail(View):

    def get(self, request, slug):
        queryset = GymLocation.objects.all()
        location = get_object_or_404(queryset, slug=slug)
        address = get_object_or_404(queryset, slug=slug)
        postcode = get_object_or_404(queryset, slug=slug)
        phone_number = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "home/locations_detail.html",
            {
                "location": location,
                "address": address,
                "postcode": postcode,
                "phone_number": phone_number,
            },
        )


def FAQs(request):
    """ returns gym locations page"""
    return render(request, "home/FAQs.html")


def payment_option(request):
    """ offers different payment options """
    offers = PaymentOption.objects.all()
    context = {
        'offers': offers
    }
    return render(request, context)


def classes(request):
    """ returns gym locations page"""
    return render(request, "home/classes.html")


def OrderMembership(request):
    """ renders subscription options """
    membership_form = MembershipForm()
    template = "home/membership.html"
    context = {
        'membership_form': membership_form,
    }

    return render(request, template, context)
