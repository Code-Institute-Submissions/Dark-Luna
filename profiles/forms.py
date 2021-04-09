"""
This is a User Profile Details form which will be
displayed in Account page - details section
"""
from django import forms
from .models import UserProfile


class UserDetailsForm(forms.ModelForm):
    """ User Details Form """
    class Meta:
        model = UserProfile
        exclude = ('user',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'postcode': 'Postcode',
            'town_or_city': 'Town or City',
            'country': 'Country',
            'county': 'County, Shire or State',
            'receiving_newsletter': 'Subscribe Newsletter',
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'country' or field == 'receiving_newsletter':
                self.fields[field].widget.attrs['placeholder'] = False
            else:
                self.fields[field].widget.attrs['placeholder'] = '...'
            self.fields[field].widget.attrs['class'] = 'user-details-fields'
