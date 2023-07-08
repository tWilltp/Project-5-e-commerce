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
    """ returns individual gym location information """
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
    """ returns FAQs page"""
    return render(request, "home/FAQs.html")


def payment_option(request):
    """ offers different payment options """
    offers = PaymentOption.objects.all()
    context = {
        'offers': offers
    }
    return render(request, context)


def classes(request):
    """ returns gym classes page"""
    classes = GymClass.objects.all()
    context = {
        'classes': classes
    }
    return render(request, "home/classes.html", context)


class classes_detail(View):

    def get(self, request, slug):
        queryset = GymClass.objects.all()
        class_name = get_object_or_404(queryset)
        schedule = get_object_or_404(queryset)

        return render(
            request,
            "home/locations_detail.html",
            {
                "class_name": class_name,
                "schedule": schedule,
            },
        )


def OrderMembership(request):
    """ renders subscription options """
    membership_form = MembershipForm()
    template = "home/membership.html"
    context = {
        'membership_form': membership_form,
        'stripe_publishable_key': 'pk_test_51NOGOUI2Zfyzau0l8ZGFhfJfMUqcpyMyBIK7bAbcNGiGsYRfZJqmOYvOTyuItHj40M7fhRMKASr5fYRpthOyC2vQ004yBAXnMl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
