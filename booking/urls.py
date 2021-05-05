""" Booking App URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('add/<workshop_id>', views.add_to_booking, name='add_to_booking'),
    path('remove/<workshop_id>', views.remove_from_booking,
         name='remove_from_booking'),
    path('clear/', views.clear_booking, name='clear_booking'),
]
