from django.contrib import admin
from .models import Category, Workshop


class CategoriesAdmin(admin.ModelAdmin):
    """ Workshop categories list display with order """
    list_display = (
        'name',
        'friendly_name',
    )

    ordering = ('name',)


class WorkshopsAdmin(admin.ModelAdmin):
    """ Lessons list display and order """
    list_display = (
        'name',
        'category',
        'participants',
        'start_date',
        'end_date',
        'start_time',
        'end_time',
        'price',
        'therapist',
    )

    ordering = ('name',)


admin.site.register(Workshop, WorkshopsAdmin)
admin.site.register(Category, CategoriesAdmin)
