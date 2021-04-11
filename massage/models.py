from django.db import models
from django.utils import timezone


class Category(models.Model):
    """ Testimonial Category Model """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=False)

    def __str__(self):
        return self.friendly_name


class Testimonial(models.Model):

    text = models.TextField()
    author = models.CharField(max_length=100)
    added = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(
        'Category', null=True, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.author
