""" Checkout App Views """
import json
import stripe

from django.conf import settings
from django.http.response import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages

from profiles.forms import UserDetailsForm
from profiles.models import UserProfile
from checkout.forms import OrderForm
from checkout.models import Order, OrderLineItem
from workshops.models import Workshop
from booking.contexts import booking_contents


@require_POST
def cache_checkout_data(request):
    """ This function will cache existing bag content """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'We are sorry that your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ A view to render checkout page """

    public_key = settings.STRIPE_PUBLIC_KEY
    secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for workshop_id, quantity in bag.items():
                try:
                    workshop = Workshop.objects.get(id=workshop_id)
                    if isinstance(quantity, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            workshop=workshop,
                            quantity=quantity,
                        )
                        order_line_item.save()
                except Workshop.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't"
                        "found in our database."
                        "Please message us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('booking'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, "There was an error with your form. \
                Check your information, please.")
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.info(request, "Your booking is empty")
            return redirect(reverse('workshops'))

        current_bag = booking_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.full_name,
                    'email': profile.email_address,
                    'phone_number': profile.phone_number,
                    'street_address1': profile.street_address1,
                    'street_address2': profile.street_address2,
                    'postcode': profile.postcode,
                    'town_or_city': profile.town_or_city,
                    'county': profile.county,
                    'country': profile.country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not public_key:
        messages.warning(request, 'Stripe public key is missing. \
                Check your environment, maybe it is there sleeping.')

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ A view to render successful checkouts """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if profile.full_name:
            if " " in profile.full_name:
                first_name = profile.full_name.split()[0]
                last_name = profile.full_name.split()[-1]
            else:
                first_name = ""
                last_name = ""
        else:
            first_name = ""
            last_name = ""

        if save_info:
            user_info = {
                'full_name': order.full_name,
                'first_name': first_name,
                'last_name': last_name,
                'email_address': order.email,
                'phone_number': order.phone_number,
                'street_address1': order.street_address1,
                'street_address2': order.street_address2,
                'postcode': order.postcode,
                'town_or_city': order.town_or_city,
                'county': order.county,
                'country': order.country,
            }
            form = UserDetailsForm(user_info, instance=profile)
            if form.is_valid():
                form.save()
            else:
                messages.error(request, form.errors)

    messages.success(
        request, f'Your order successfully has been processed. \
            Order number: {order_number} \
            Check your email and confirmation we have sent to {order.email}.')
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
