from django.shortcuts import render
from massage.models import Testimonial


def index(request):
    """ A view to return index page """
    testimonial = Testimonial.objects.all()

    context = {
        'testimonials': testimonial,
    }

    return render(request, 'shadow/shadow.html', context)
