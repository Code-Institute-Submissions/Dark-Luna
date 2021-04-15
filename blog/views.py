from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .forms import PostForm


class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AddBlogPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_blog.html'
    fields = ['title', 'tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('blog')
