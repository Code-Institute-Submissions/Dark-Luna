from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,
                                     upload_to="user_uploads/")
    tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    snippet = models.CharField(max_length=166)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    source = models.CharField(max_length=255, blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-post-detail', args=(str(self.id),))


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments",
                             on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def get_absolute_url(self):
        return reverse('blog')
