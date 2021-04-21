"""
This module will render user account page with
all necessary user information and forms
"""
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView)
from profiles.forms import (
                            UserDetailsForm,
                            TestimonialForm,
                            TestimonialEditForm)
# from checkout.models import Order
from .models import UserProfile, Testimonial


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
    # orders = profile.orders.all().order_by('-id')[:10]

    template = 'account/account.html'
    context = {
        'form': details_form,
        # 'orders': orders,
        'no_bag': True,
    }
    return render(request, template, context)


class TestimonialHomeView(ListView):
    model = Testimonial
    template_name = 'account/testimonial_list.html'


class AddTestimonialView(CreateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'account/testimonial_form.html'


class UpdateTestimonialView(UpdateView):
    model = Testimonial
    form_class = TestimonialEditForm
    template_name = 'account/update_testimonial.html'


class DeleteTestimonialView(DeleteView):
    model = Testimonial
    success_url = reverse_lazy('user_account')


# @login_required(login_url='/accounts/login/')
# def booking_review(request, order_number):
#     """ A view to return booking information """
#     # order = get_object_or_404(Order, order_number=order_number)/workspace/.pip-modules/lib/python3.8/site-packages/crispy_forms/templatetags/crispy_forms_filters.py
#     return render(request, template, context)


# @login_required(login_url='/accounts/login/')
# def bookings_active(request):
#     """ A view to return user active bookings """

#     profile = get_object_or_404(UserProfile, user=request.user)

#     # Order user orders - newest at begining
#     user_orders = profile.orders.all()

#     # Filter Booking orders between today and past 60 days - including today's bookings
#     start_date = date.today() + timedelta(days=1)
#     end_date = start_date + timedelta(days=-59)
#     # Filter date range
#     user_orders = user_orders.filter(date__range=[end_date, start_date])

#     # Sort orders by date - newset first
#     user_orders = user_orders.order_by('-date')

#     from_booking_active = True
#     request.session['from_booking_active'] = from_booking_active

#     # Send number of active bookings to session
#     request.session['active_booking_count'] = user_orders.count()

#     template = 'account/bookings-active.html'
#     context = {
#         'user_orders': user_orders,
#         'from_booking_active': from_booking_active,
#     }

#     return render(request, template, context)


# @login_required(login_url='/accounts/login/')
# def bookings_archived(request):
#     """ A view to return user archived bookings """

#     profile = get_object_or_404(UserProfile, user=request.user)

#     # Order user orders - newest at begining
#     user_orders = profile.orders.all()

#     # Filter Booking older than 60 days
#     start_date = date.today() + timedelta(days=-59)
#     end_date = start_date + timedelta(days=-365)
#     # Filter date range
#     user_orders = user_orders.filter(date__range=[end_date, start_date])

#     # Sort orders by date - newset first
#     user_orders = user_orders.order_by('-date')

#     from_booking_archived = True
#     request.session['from_booking_archived'] = from_booking_archived

#     # Get active booking count
#     active_booking_count = request.session.get('active_booking_count')

#     template = 'account/bookings-archived.html'
#     context = {
#         'user_orders': user_orders,
#         'from_booking_archived': from_booking_archived,
#         'active_booking_count': active_booking_count,
#     }

    # return render(request, template, context)
