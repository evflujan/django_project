
from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /books/
    path('books/', views.books, name='books'),
    # ex: /book/<id>/
    path('book/<int:book_id>', views.book, name='book'), #book_view
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),


    # ex: /authors/
    path('authors/', views.authors, name='authors'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    # ex: /author/<id>/
    path('author/<int:author_id>', views.author, name='author'),
    # ex: /author/<id>/books/
    path('author/<int:author_id>/books/', views.author_books, name='author_books'),
]
