""" Models for Profiles App """
from django.db import models
from django.db.models.fields import CharField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

from django.contrib.auth.models import User


class UserProfile(models.Model):
    """ User Profile model to maintain
    current bookings, history of bookings """

    class Meta:
        verbose_name_plural = 'Users Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = CharField(max_length=200,  blank=True)
    first_name = models.CharField(max_length=100,  blank=True)
    last_name = models.CharField(max_length=100,  blank=True)
    email_address = models.EmailField(max_length=254, null=False, blank=True)
    phone_number = models.CharField(
        max_length=20,  blank=True)
    street_address1 = models.CharField(
        max_length=80,  blank=True)
    street_address2 = models.CharField(
        max_length=80,  blank=True)
    postcode = models.CharField(max_length=20,  blank=True)
    town_or_city = models.CharField(
        max_length=40,  blank=True)
    county = models.CharField(max_length=80,  blank=True)
    country = CountryField(
        blank_label='Select Country',  blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create/update user profile """

    if created:
        UserProfile.objects.create(user=instance)
    # if user exist - save the profile
    instance.userprofile.save()
