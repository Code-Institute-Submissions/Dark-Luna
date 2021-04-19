from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post, Category
from .forms import PostForm
from django.http import HttpResponseRedirect


class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    ordering = ['-post_date']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)

        likes = get_object_or_404(Post, id=self.kwargs['pk'], )
        total_likes = likes.total_likes()

        liked = False
        if likes.likes.filter(id=self.request.user.id):
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddBlogPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'


def CategoryView(request, cats):
    category_posts = Post.objects.filter(
        category__iexact=cats.replace('-', ' '))
    return render(request, 'blog/categories.html',
                  {'cats': cats.title().replace('-', ' '),
                   'category_posts': category_posts})


class AddCategoryView(CreateView):
    model = Category
    template_name = 'blog/category_form.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_blog.html'
    fields = ['title', 'tag', 'body', 'category']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('blog')


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('blog-post-detail', args=[str(pk)]))
