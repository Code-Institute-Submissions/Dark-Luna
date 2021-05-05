"""
This module will render user account page with
all necessary user information and forms
"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.forms import (UserDetailsForm)
from checkout.models import Order
from .models import UserProfile


@login_required(login_url='/accounts/login/')
def user_account(request):
    """ A view to return account page """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details updated successfully!')

    details_form = UserDetailsForm(instance=profile)
    orders = profile.orders.all().order_by('-id')[:10]

    template = 'account/account.html'
    context = {
        'form': details_form,
        'orders': orders,
        'no_bag': True,
    }
    return render(request, template, context)


@login_required(login_url='/accounts/login/')
def booking_review(request, order_number):
    """ A view to return booking information """
    order = get_object_or_404(Order, order_number=order_number)
    workshops_count = order.lineitems.count()

    template = 'account/bookings-review.html'
    context = {
        'order': order,
        'workshops_count': workshops_count
    }
    return render(request, template, context)
