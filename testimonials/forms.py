from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    """ Testimonials Form """
    class Meta:
        model = Testimonial
        fields = (
            'text', 'page',
        )

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs = {'rows': 3}
        for field in self.fields:
            if field == 'page':
                self.fields[field].widget.attrs['placeholder'] = False
            else:
                self.fields[field].widget.attrs['placeholder'] = '...'
                self.fields[field].widget.attrs['class'] = 'add-form-input'
