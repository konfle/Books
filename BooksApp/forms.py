from django import forms
from django.forms import TextInput

from .models import PostBook


class BooksCreateForm(forms.ModelForm):

    class Meta:
        model = PostBook
        fields = ('title', 'author', 'published_date', 'isbn_number', 'page_count', 'cover_link', 'language')
        widgets = {
            'title': TextInput(attrs={'class': 'input--style-6', 'placeholder': 'Book title'}),
            'author': TextInput(attrs={'class': 'input--style-6', 'placeholder': 'Book author'}),
            'published_date': TextInput(attrs={'class': 'input--style-6', 'placeholder': 'Publish date'}),
            'isbn_number': TextInput(attrs={'class': 'input--style-6', 'placeholder': 'ISBN number'}),
            'page_count': TextInput(attrs={'class': 'input--style-6', 'placeholder': 'Amount of pages'}),
            'cover_link': TextInput(attrs={'class': 'input--style-6', 'placeholder': 'Link to cover'}),
            'language': TextInput(attrs={'class': 'input--style-6', 'placeholder': 'Book language'}),
        }
