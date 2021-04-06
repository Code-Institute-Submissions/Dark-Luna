from django.shortcuts import render
from .models import Video


def video(request):
    videos = Video.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'videos/videos.html', context)
