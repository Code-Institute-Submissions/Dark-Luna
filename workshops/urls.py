""" Workshops App URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.workshops, name='workshops'),
    path('<workshop_id>', views.workshop, name='workshop'),
    # Management Categories  Url's
    path('management/lessons-page/categories',
         views.categories_management, name='categories_management'),
    path('management/workshops-page/categories/add',
         views.add_categories_management, name='add_categories_management'),
    path('management/workshops-page/categories/edit/<int:category_id>',
         views.edit_categories_management, name='edit_categories_management'),
    path('management/workshops-page/categories/remove/<int:category_id>',
         views.remove_categories_management,
         name='remove_categories_management'),
    # Management Workshops Url's
    path('management/workshops-page/workshops',
         views.workshops, name='workshops_management'),
    path('management/workshops-page/workshops/add',
         views.add_workshops_management, name='add_workshops_management'),
    path('management/workshops-page/workshops/edit<int:workshop_id>',
         views.edit_workshops_management, name='edit_workshops_management'),
    path('management/workshops-page/workshops/remove/<int:workshop_id>',
         views.remove_workshops_management,
         name='remove_workshops_management'),
]