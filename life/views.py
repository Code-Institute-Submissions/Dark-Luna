from django.shortcuts import render
from testimonials.models import Testimonial


def index(request):
    """ A view to return index page """
    testimonial = Testimonial.objects.all()

    context = {
        'testimonials': testimonial,
    }

    return render(request, 'life/life.html', context)
