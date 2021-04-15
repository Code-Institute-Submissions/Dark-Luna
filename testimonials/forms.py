from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    """ Testimonials Form """
    class Meta:
        model = Testimonial
        fields = (
            'text', 'page', 'author',
        )
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'page': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'})
        }

