from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Testimonial(models.Model):
    """ Level Cards Model - for users """
    class RelatedPage(models.TextChoices):
        """ Choices for dropdown list in page """
        Massage = 'Massage'
        Sex_Coaching = 'Sex Coaching'
        Life_Coaching = 'Life Coaching'
        Shadow_Work = 'Shadow Work'
        Workshops = 'Workshops'

    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    added = models.DateTimeField(default=timezone.now)
    page = models.CharField(choices=RelatedPage.choices,
                            default=RelatedPage.Massage, max_length=13)

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('user_account')
