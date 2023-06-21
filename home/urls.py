from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path(
        'home/locations.html/', views.locations, name="locations"),
    path('home/FAQs.html/', views.FAQs, name="FAQs"),
]
