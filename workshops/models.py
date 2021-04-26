""" Models for Workshops App """
from django.db import models


class Category(models.Model):
    """ Workshops Category Model """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=False)

    def __str__(self):
        return self.friendly_name


class Workshop(models.Model):
    """ Workshop Model """
    name = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=False, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=False)
    end_date = models.DateField(null=True, blank=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    participants = models.IntegerField(null=True, blank=False)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=False)
    image = models.ImageField(blank=True, null=True,
                              upload_to="user_uploads/")
    therapist = models.CharField(max_length=254)

    def __str__(self):
        return self.name
