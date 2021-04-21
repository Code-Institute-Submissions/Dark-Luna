from django.shortcuts import render
# from .models import Testimonial
# import random
# from django.contrib.admin.views.decorators import staff_member_required
# from massage.forms import TestimonialForm


def index(request):
    """ A view to return index page """
    # testimonial = Testimonial.objects.all()
    # random_testimonial = random.choice(testimonial)

    # context = {
    #     'random_testimonial': random_testimonial,
    # }

    return render(request, 'massage/massage.html')
