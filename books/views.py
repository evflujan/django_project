from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author, Book
# Create your views here.

def index(request):
  template = loader.get_template('books/index.html')
  context = {}
  return HttpResponse(template.render(context, request))

def books(request):
  book_list = Book.objects.order_by('title')
  template = loader.get_template('books/books.html')
  context = { 'book_list': book_list }
  return HttpResponse(template.render(context, request))

def book(request, book_id):
  book = Book.objects.get(pk=book_id)
  author = Author.objects.get(pk=book.author_id)
  template = loader.get_template('books/book.html')
  context = {'book': book, 'author': author}
  return HttpResponse(template.render(context, request))

def authors(request):
  author_list = Author.objects.order_by('name')
  template = loader.get_template('books/authors.html')
  context = { 'author_list': author_list }
  return HttpResponse(template.render(context, request))

def author(request, author_id ):
  author = Author.objects.get(pk=author_id)
  template = loader.get_template('books/author.html')
  context = { 'author': author }
  return HttpResponse(template.render(context, request))

def author_books(request, author_id):
  author = Author.objects.get(pk=author_id)
  author_books = Book.objects.filter(author=author_id)
  template = loader.get_template('books/author_books.html')
  context = {'author_books': author_books, 'author': author}
  return HttpResponse(template.render(context, request))
