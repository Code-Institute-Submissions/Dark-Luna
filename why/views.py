from django.shortcuts import render


def why(request):
    """ A view to return index page """

    return render(request, 'why/why.html')
