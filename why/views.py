from django.shortcuts import render
from videos.models import Video


def index(request):
    """ A view to return index page """
    videos = Video.objects.all().filter(title="Let's Get Naked")
    context = {
        'videos': videos,
    }
    return render(request, 'why/why.html', context)
