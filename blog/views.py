# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# def index(request):
#     """ A view to return index page """

#     return render(request, 'blog/blog.html', {})

class BlogHomeView(ListView):
    model = Post
    template = 'blog/blog.html'
