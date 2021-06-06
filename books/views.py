from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.template import loader
from .models import Author, Book
from .forms import BookForm, AuthorForm
# Create your views here.

def index(request):
  template = 'books/index.html'
  context = {}
  return render(request, template, context)

def books(request):
  template = 'books/book_list.html'
  book_list = Book.objects.order_by('title')
  context = { 'book_list': book_list }
  return render(request, template, context)

def book(request, book_id):
  template = 'books/book_detail.html'
  book = Book.objects.get(pk=book_id)
  author = Author.objects.get(pk=book.author_id)
  context = {'book': book, 'author': author}
  return render(request, template, context)


class BookCreate(LoginRequiredMixin, View):
    template = 'books/book_form.html'
    success_url = reverse_lazy('books:books')

    def get(self, request):
        form = BookForm()
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request):
        form = BookForm(request.POST)
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template, context)
        book = form.save()
        return redirect(self.success_url)



class BookUpdate(LoginRequiredMixin, View):
    model = Book
    success_url = reverse_lazy('books:books')
    template = 'books/book_form.html'

    def get(self, request, pk):
        book = get_object_or_404(self.model, pk=pk)
        form = BookForm(instance=book)
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request, pk):
        book = get_object_or_404(self.model, pk=pk)
        form = BookForm(request.POST, instance=book)
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template, context)

        form.save()
        return redirect(self.success_url)



class BookDelete(LoginRequiredMixin, View):
    model = Book
    success_url = reverse_lazy('books:books')
    template = 'books/book_confirm_delete.html'
    def get(self, request, pk):
        book = get_object_or_404(self.model, pk=pk)
        form = BookForm(instance=book)
        context = {'book': book}
        return render(request, self.template, context)

    def post(self, request, pk):
        book = get_object_or_404(self.model, pk=pk)
        book.delete()
        return redirect(self.success_url)




def authors(request):
  template = 'books/author_list.html'
  author_list = Author.objects.order_by('name')
  context = { 'author_list': author_list }
  return render(request, template, context)


class AuthorCreate(LoginRequiredMixin, View):
    template = 'books/author_form.html'
    success_url = reverse_lazy('books:authors')

    def get(self, request):
        form = AuthorForm()
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request):
        form = AuthorForm(request.POST)
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template, context)
        book = form.save()
        return redirect(self.success_url)


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('books:authors')


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('books:authors')



def author(request, author_id ):
  template = 'books/author_detail.html'
  author = Author.objects.get(pk=author_id)
  context = { 'author': author }
  return render(request, template, context)

def author_books(request, author_id):
  template = 'books/author_books.html'
  author = Author.objects.get(pk=author_id)
  author_books = Book.objects.filter(author=author_id)
  context = {'author_books': author_books, 'author': author}
  return render(request, template, context)
