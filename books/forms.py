from django import forms
from django.forms import ModelForm
from books.models import Book, Author

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
