from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author, Book
from django.views import generic
# Create your views here.

def index(request):
  template = 'books/index.html'
  context = {}
  return render(request, template, context)
'''
def books(request):
  template = 'books/books.html'
  book_list = Book.objects.order_by('title')
  context = { 'book_list': book_list }
  return render(request, template, context)

def book(request, book_id):
  template = 'books/book.html'
  book = Book.objects.get(pk=book_id)
  author = Author.objects.get(pk=book.author_id)
  context = {'book': book, 'author': author}
  return render(request, template, context)
'''
class BookListView(generic.ListView):
  model = Book

class BookDetailView(generic.DetailView):
  model = Book

'''
def authors(request):
  template = 'books/authors.html'
  author_list = Author.objects.order_by('name')
  context = { 'author_list': author_list }
  return render(request, template, context)

def author(request, author_id ):
  template = 'books/author.html'
  author = Author.objects.get(pk=author_id)
  context = { 'author': author }
  return render(request, template, context)
'''

class AuthorListView(generic.ListView):
  model = Author

class AuthorDetailView(generic.DetailView):
  model = Author


def author_books(request, author_id):
  template = 'books/author_books.html'
  author = Author.objects.get(pk=author_id)
  author_books = Book.objects.filter(author=author_id)
  context = {'author_books': author_books, 'author': author}
  return render(request, template, context)
