from django.views.generic import CreateView
from .models import Testimonial
from .forms import TestimonialForm


class AddTestimonial(CreateView):
    model = Testimonial
    form_class = TestimonialForm
    template = 'testimonials/testimonial_form.html'
