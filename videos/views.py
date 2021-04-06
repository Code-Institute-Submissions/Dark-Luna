from django.shortcuts import render
from .models import Video


def video(request):
    video = Video.objects.all()
    context = {
        'video': video,
    }
    return render(request, 'videos/videos.html', context)
