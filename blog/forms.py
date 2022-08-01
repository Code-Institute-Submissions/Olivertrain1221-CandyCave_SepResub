from django import forms
from .models import Posts


class BlogForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ('author', 'slug',)