""" Views for Booking App """
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from workshops.models import Workshop


def booking(request):
    """ A view to return booking page """

    return render(request, 'booking/booking.html')


def add_to_booking(request, workshop_id):
    """ A view to add a workshop to the booking_bag """

    workshop = Workshop.objects.get(pk=workshop_id)
    quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if workshop_id in list(bag.keys()):
        messages.warning(
            request, f'{ workshop.name } already exists in your booking!')
    else:
        bag[workshop_id] = quantity
        messages.success(
            request, f'{ workshop.name } added successfully to your booking!')

    request.session['bag'] = bag
    return redirect('booking')


def remove_from_booking(request, workshop_id):
    """ A view to remove workshop(s) from the booking 'bag' """

    try:
        workshop = Workshop.objects.get(pk=workshop_id)
        bag = request.session.get('bag', {})
        bag.pop(workshop_id)
        messages.info(
            request, f'{ workshop.name } removed successfully from booking!')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request, f'Error while removing workshop: {e}')
        return HttpResponse(status=500)


def clear_booking(request):
    """ A view to clear whole content from booking 'bag' """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    bag.clear()
    request.session['bag'] = bag

    messages.info(
        request, 'Your booking has been cleared successfully!')

    return redirect(redirect_url)
