from django.contrib import admin

from .models import Testimonial


class TestimonialsAdmin(admin.ModelAdmin):
    """ Lessons Card admin list display and ordering """

    list_display = (
        'text',
        'author',
        'added',
    )

    ordering = ('author',)


admin.site.register(Testimonial, TestimonialsAdmin)
