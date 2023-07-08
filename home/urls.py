from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('home/locations.html/', views.LocationsView, name='locations'),
    path('<slug:slug>/', views.locations_detail.as_view(
        ), name='locations_detail'),
    # path('home/locations_detail', views.classes_detail.as_view(
    #     ), name='classes_detail'),
    path('home/FAQs.html/', views.FAQs, name="FAQs"),
    path('home/classes.html/', views.classes, name="classes"),
    path('home/membership.html', views.OrderMembership, name='membership'),
]
