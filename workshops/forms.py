from django import forms
from .models import Category, Workshop


class CategoriesForm(forms.ModelForm):
    """ Categories form """
    class Meta:
        model = Category
        fields = ('name', 'friendly_name',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = '...'
            self.fields[field].widget.attrs['class'] = 'add-form-input'


class WorkshopsForm(forms.ModelForm):
    """ Lessons form """
    class Meta:
        model = Workshop
        fields = (
            'name', 'category',
            'description', 'start_date', 'end_date',
            'start_time', 'end_time', 'participants',
            'price', 'image', 'therapist',
        )
        labels = {
            'image': 'Add Image',
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': '...',
            'category': '...',
            'description': '...',
            'start_date': 'YYYY-MM-DD',
            'end_date': 'YYYY-MM-DD',
            'start_time': 'HH:MM:SS',
            'end_time': 'HH:MM:SS',
            'participants': 'Number of Participants',
            'price': '150',
            'image': '...',
            'therapist': '...',
        }

        self.fields['description'].widget.attrs = {'rows': 3}
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            if field == 'image' or field == 'category':
                self.fields[field].widget.attrs['placeholder'] = False
            else:
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'add-form-input'
