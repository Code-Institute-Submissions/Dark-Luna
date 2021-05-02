""" Apps registered in Administration from Team App """
from django.contrib import admin
from .models import TherapistProfile


class TherapistProfileAdmin(admin.ModelAdmin):
    """ Therapists Profiles admin list display and ordering """
    list_display = (
        'name',
        'age',
        'about',
    )

    ordering = ('name',)


admin.site.register(TherapistProfile, TherapistProfileAdmin)
