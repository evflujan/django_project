
from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /books/
    path('books/', views.BookListView.as_view(), name='books'),
    # ex: /book/<id>/
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book'),
    # ex: /authors/
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    # ex: /author/<id>/
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author'),
    # ex: /author/<id>/books/
    path('author/<int:author_id>/books/', views.author_books, name='author_books'),
]
