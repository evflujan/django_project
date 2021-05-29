
from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /books/
    path('books/', views.books, name='books'),
    # ex: /book/<id>/
    path('book/<int:book_id>', views.book, name='book'),
    # ex: /authors/
    path('authors/', views.authors, name='authors'),
    # ex: /author/<id>/
    path('author/<int:author_id>', views.author, name='author'),
    # ex: /author/<id>/books/
    path('author/<int:author_id>/books/', views.author_books, name='author_books'),
]
