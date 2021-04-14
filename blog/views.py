# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class BlogHomeView(ListView):
    model = Post
    template = 'blog/post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template = 'blog/post_detail.html'


class AddBlogPost(CreateView):
    model = Post
    template = 'blog/post_form.html'
    fields = '__all__'
