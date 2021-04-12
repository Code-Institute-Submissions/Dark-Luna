from django.db import models
from django.utils import timezone


# class Testimonial(models.Model):
#     """ Level Cards Model - for users """
#     class RelatedPage(models.TextChoices):
#         """ Choices for dropdown list in Level Cards """
#         Massage = 'Massage'
#         Sex_Coaching = 'Sex Coaching'
#         Life_Coaching = 'Life Coaching'
#         Shadow_Work = 'Shadow Work'
#         Workshops = 'Workshops'

#     text = models.TextField()
#     author = models.CharField(max_length=100)
#     added = models.DateTimeField(default=timezone.now)
#     page = models.CharField(choices=RelatedPage.choices,
#                             default=RelatedPage.Massage, max_length=13)

#     def __str__(self):
#         return self.author
