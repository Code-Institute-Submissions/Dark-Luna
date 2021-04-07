from django.shortcuts import render
from videos.models import Video


def index(request):
    """ A view to return index page """
    
    return render(request, 'why/why.html')
