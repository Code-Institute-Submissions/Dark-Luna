from django.db import models

from embed_video.fields import EmbedVideoField


class Video(models.Model):
    title = models.CharField(max_length=100)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)


class Meta:
    verbose_name_plural = "Videos"
