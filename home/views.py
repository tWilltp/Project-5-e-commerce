from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import GymLocation, EquipmentFacilities, PaymentOption, GymClass
from .forms import MembershipForm
from django.conf import settings
import stripe


def index(request):
    """ returns index page """
    return render(request, "home/index.html")


def equipment_and_facilities(request):
    """ returns gym equipment and facilities on locations detail page"""
    equipment_facilities = EquipmentFacilities.objects.all()
    context = {
        "equipment_facilities": equipment_facilities,
    }
    return render(request, "home/locations_detail.html", context)


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
        classes = get_object_or_404(queryset, slug=slug)
        class_schedule = get_object_or_404(queryset, slug=slug)
        equipment_facilities = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "home/locations_detail.html",
            {
                "location": location,
                "address": address,
                "postcode": postcode,
                "phone_number": phone_number,
                "classes": classes,
                "class_schedule": class_schedule,
                "equipment_facilities": equipment_facilities,
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


def lifestyle(request):
    """ returns lifestyle page"""
    return render(request, "home/lifestyle.html")


def OrderMembership(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key
    stripe_total = int('26')*100
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    """ renders subscription options """
    membership_form = MembershipForm()
    template = "home/membership.html"
    context = {
        'membership_form': membership_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
