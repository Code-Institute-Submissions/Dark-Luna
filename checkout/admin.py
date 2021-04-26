""" Checkout app Admin """
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderInlineItemAdmin(admin.TabularInline):
    """ Class to view a workshop in admin order view """
    model = OrderLineItem
    readonly_fields = ('lineitem_total', 'quantity',)


class OrderAdmin(admin.ModelAdmin):
    """ Class to view a order in admin view """
    inlines = (OrderInlineItemAdmin,)

    readonly_fields = ('order_number', 'date',
                       'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date',
              'full_name', 'email', 'phone_number',
              'street_address1', 'street_address2', 'postcode',
              'town_or_city', 'county', 'country',
              'order_total', 'grand_total',
              'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
