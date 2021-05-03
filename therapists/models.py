""" Therapists App Models """
from django.db import models


class TherapistProfile(models.Model):
    """ Instructor Profile Card Model """
    class Meta:
        verbose_name_plural = 'Therapists Profiles'

    name = models.CharField(max_length=254, blank=False)
    about = models.TextField(null=True, blank=False)
    image = models.ImageField(upload_to="instructors", null=True, blank=True)

    def __str__(self):
        return self.name
