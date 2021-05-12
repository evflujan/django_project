from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  return HttpResponse("Esta es la primera página (index) de la aplicación books")

def books(request):
  response = 'Ha solicitado la lista de todos los libros'
  return HttpResponse(response)

def book(request, book_id):
  response = 'Ha solicitado la información del libro %s'
  return HttpResponse(response % book_id)

def authors(request):
  response = 'Ha solicitado la lista de todos los autores'
  return HttpResponse(response)

def author(request, author_id ):
  response = 'Ha solicitado la información del autor %s'
  return HttpResponse(response % author_id)

def author_books(request, author_id):
  response = 'Ha solicitado los libros publicados por el autor %s'
  return HttpResponse(response % author_id)
