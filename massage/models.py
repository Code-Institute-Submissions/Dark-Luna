from django.db import models
from django.utils import timezone


class Testimonial(models.Model):

    text = models.TextField()
    author = models.CharField(max_length=100)
    added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author
