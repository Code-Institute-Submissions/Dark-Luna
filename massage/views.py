from django.shortcuts import render
from .models import Testimonial
# from django.contrib.admin.views.decorators import staff_member_required
# from massage.forms import TestimonialForm


def index(request):
    """ A view to return index page """
    testimonial = Testimonial.objects.all()

    context = {
        'testimonials': testimonial,
    }

    return render(request, 'massage/massage.html', context)
