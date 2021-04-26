from django import forms
from .models import Post, Category, Comment


# choices = Category.objects.all(). values_list('name', 'name')

choice_list = []

# for item in choices:
#     choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'body', 'author',
                  'snippet', 'category', 'header_image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,
                                     attrs={'class': 'form-control'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'body', 'snippet', 'header_image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body',)

        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
