from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post, Category
from .forms import PostForm


class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    ordering = ['-post_date']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AddBlogPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'blog/categories.html', {'cats': cats.title(),
                                                    'category_posts': category_posts})


class AddCategoryView(CreateView):
    model = Category
    template_name = 'blog/category_form.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_blog.html'
    fields = ['title', 'tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('blog')
