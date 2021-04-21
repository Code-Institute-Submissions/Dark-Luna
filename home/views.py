from django.views.generic import ListView
from blog.models import Post
from profile.models import Testimonial


class BlogHomeView(ListView):
    model = Post
    template_name = 'home/index.html'
    ordering = ('-post_date')


class TestimonialHomeView(ListView):
    model = Testimonial
    template_name = 'home/index.nl'
