""" Booking Bag Contexts """
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from workshops.models import Workshop


def booking_contents(request):
    """
    This function will allow to use booking
    contents 'bag' on whole application
    """

    booked_workshops = []
    total = 0
    workshops_count = 0
    bag = request.session.get('bag', {})

    for workshop_id, quantity in bag.items():
        workshop = get_object_or_404(Workshop, pk=workshop_id)
        total += quantity * workshop.price
        workshops_count += quantity
        booked_workshops.append({
            'workshop_id': workshop_id,
            'quantity': quantity,
            'workshop': workshop,
        })

    grand_total = total

    context = {
        'booked_workshops': booked_workshops,
        'total': total,
        'workshops_count': workshops_count,
        'grand_total': grand_total,
        'bag': bag,
    }

    return context