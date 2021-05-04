""" Workshops App URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.workshops, name='workshops'),

    path('<workshop_id>', views.workshop, name='workshop'),

    # Admin Categories  Url's
    path('admin/workshops-page/categories',
         views.categories_admin, name='categories_admin'),

    path('admin/workshops-page/categories/add/',
         views.add_categories_admin, name='add_categories_admin'),

    path('admin/workshops-page/categories/edit/<int:category_id>',
         views.edit_categories_admin, name='edit_categories_admin'),

    path('admin/workshops-page/categories/remove/<int:category_id>',
         views.remove_categories_admin,
         name='remove_categories_admin'),

    # Admin Workshops Url's
    path('admin/workshops-page/workshops',
         views.workshops_admin, name='workshops_admin'),

    path('admin/workshops-page/workshops/add/',
         views.add_workshops_admin, name='add_workshops_admin'),

    path('admin/workshops-page/workshops/edit/<int:workshop_id>',
         views.edit_workshops_admin, name='edit_workshops_admin'),

    path('admin/workshops-page/workshops/remove/<int:workshop_id>',
         views.remove_workshops_admin,
         name='remove_workshops_admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
