# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


class BlogHomeView(ListView):
    model = Post
    template = 'blog/post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template = 'blog/post_detail.html'


class AddBlogPost(CreateView):
    model = Post
    form_class = PostForm
    template = 'blog/post_form.html'

