from django.shortcuts import render


def about(request):
    """ A view to return index page """

    return render(request, 'how/how.html')
