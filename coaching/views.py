from django.shortcuts import render


def index(request):
    """ A view to return the coaching page """

    return render(request, 'coaching/coaching.html')
