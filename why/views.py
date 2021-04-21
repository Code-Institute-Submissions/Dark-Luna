from django.shortcuts import render
from massage.models import Testimonial


def index(request):
    """ A view to return index page """
    testimonial = Testimonial.objects.all()

    context = {
        'testimonials': testimonial,
    }

    return render(request, 'why/why.html', context)

# class AddTestimonial(CreateView):
#     model = Testimonial
#     form_class = TestimonialForm
#     template_name = 'blog/post_form.html'
