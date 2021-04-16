from django.views.generic import ListView
from blog.models import Post


class BlogHomeView(ListView):
    model = Post
    template_name = 'home/index.html'
    ordering = ['-post_date']
