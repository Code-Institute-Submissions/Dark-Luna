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


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'body',
                  'snippet', 'author', 'category', 'header_image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,
                                     attrs={'class': 'form-control'})
        }