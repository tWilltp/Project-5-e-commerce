from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('home/locations.html/', views.LocationsView, name='locations'),
    path('home/locations_detail.html/', views.locations_detail, name='locations_detail'),
    path('home/FAQs.html/', views.FAQs, name="FAQs"),
]
