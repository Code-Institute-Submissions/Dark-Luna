from django.contrib import admin

from testimonials.models import Testimonial


class TestimonialsAdmin(admin.ModelAdmin):
    """ Testimonials admin list display and ordering """

    list_display = (
        'author',
        'text',
        'added',
        'page'
    )

    ordering = ('author',)


admin.site.register(Testimonial, TestimonialsAdmin)
