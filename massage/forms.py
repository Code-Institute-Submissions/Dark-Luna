from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    """ Testimonials form """
    class Meta:
        model = Testimonial
        fields = ('text', 'author',
                  )

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs = {'rows': 3}
        self.fields['author'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = '...'
            self.fields[field].widget.attrs['class'] = 'add-form-input'
