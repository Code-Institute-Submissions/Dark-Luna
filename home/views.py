from django.shortcuts import render

from .models import Video


def index(request):
    """ A view to return index page """
    videos = Video.objects.all()

    context = {
        'videos': videos,
    }
    return render(request, 'home/index.html', context)
