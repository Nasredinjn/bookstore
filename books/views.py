from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import *


class BookListView(ListView):
    template_name = "books/books_list.html"
    model = Book
    context_object_name = "books"


class BookDetailsList(DetailView):
    template_name = "books/book_details.html"
    model = Book
    context_object_name = "book"
    def get_context_data(self, **kwargs):
        context = super(BookDetailsList, self).get_context_data()
        context["reviews"] = self.object.book_reviews.all()
        return context