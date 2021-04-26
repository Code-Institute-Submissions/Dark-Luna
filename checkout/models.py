""" Models for Checkout App """

import uuid

from datetime import datetime
from django.db import models
from django.db.models import Sum
# from django.conf import settings

from django_countries.fields import CountryField

from workshops.models import Workshop
from profiles.models import UserProfile


class Order(models.Model):
    """ This is ored model used to create orders """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Select Country *',
                           null=False, blank=False)
    date = models.DateTimeField(default=datetime.now)
    order_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _create_order_number(self):
        """ This function will create a random,/
        unique order number by using UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update grand total when new item is added, include discount. """

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))[
            'lineitem_total__sum'] or 0
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """ This function will override the orignal save method and
        create the order number if it hasn't been created before """

        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """ This is a function which will create
    a single item on order
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    workshop = models.ForeignKey(Workshop, null=False,
                                 blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    # Quantity field is created to take higher number than 1 as customer
    # can change the way of purchasing workshops and/
    # quantities for each workshop
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ This function will override the orignal save method to set the """

        self.lineitem_total = self.workshop.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Name {self.workshop.name} on Order {self.order.order_number}'
