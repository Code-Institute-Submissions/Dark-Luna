from django.views.generic import ListView
from blog.models import Post


class BlogHomeView(ListView):
    model = Post
    template_name = 'home/index.html'
    # ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        Post.objects.all()[:2]
        context = super(BlogHomeView, self).get_context_data(*args, **kwargs)
        return context
