""" Webhooks Handlers for Checkout App """

import json
import time

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from checkout.models import Order, OrderLineItem
from workshops.models import Workshop


class StripeWhHandler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        print(order)
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        pid = intent.id
        print(pid)
        bag = intent.metadata.bag

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.full_name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone_number,
                    street_address1__iexact=(
                        billing_details.address.street_address1),
                    street_address2__iexact=(
                        billing_details.address.street_address1),
                    town_or_city__iexact=billing_details.address.town_or_city,
                    postcode__iexact=billing_details.address.postcode,
                    county__iexact=billing_details.address.county,
                    country__iexact__iexact=billing_details.address.country,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.full_name,
                    email=billing_details.email,
                    phone_number=billing_details.phone_number,
                    street_address1=billing_details.street_address1,
                    street_address2=billing_details.street_address1,
                    town_or_city=billing_details.town_or_city,
                    postcode=billing_details.postcode,
                    county=billing_details.county,
                    country=billing_details.country,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for workshop_id, quantity in json.loads(bag).items():
                    workshop = Workshop.objects.get(id=workshop_id)
                    if isinstance(quantity, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            workshop=workshop,
                            quantity=quantity,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
