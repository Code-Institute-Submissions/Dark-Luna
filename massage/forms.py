from django import forms
from .models import Testimonial


Category = [
    ('massage', 'Massage'),
    ('sex-coaching', 'Sex Coaching'),
    ('life-coaching', 'Life Coaching'),
    ('shadow-coaching', 'Shadow Coaching'),
    ('workshops', 'Workshops'),
    ]


class TestimonialForm(forms.ModelForm):
    """ Testimonials form """
    class Meta:
        model = Testimonial
        fields = ('text', 'author', 'category',
                  )
    Category = forms.CharField(label='Category',
                               widget=forms.Select(choices=Category))

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs = {'rows': 3}
        self.fields['author'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = '...'
            self.fields[field].widget.attrs['class'] = 'add-form-input'
