from django.shortcuts import render
from videos.models import Video


def index(request):
    """ A view to return index page """
    videos = Video.objects.all().filter(title="My Revolution Lives In This Body")
    context = {
        'videos': videos,
    }
    return render(request, 'home/index.html', context)
