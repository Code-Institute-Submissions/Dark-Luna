from django.contrib import admin

from .models import Testimonial


class TestimonialsAdmin(admin.ModelAdmin):
    """ Lessons Card admin list display and ordering """

    list_display = (
        'author',
        'text',
        'added',
        'category'
    )

    ordering = ('author',)


admin.site.register(Testimonial, TestimonialsAdmin)
