from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class BookListView(LoginRequiredMixin, ListView):
    template_name = "books/books_list.html"
    model = Book
    context_object_name = "books"
    login_url = "account_login"


class BookDetailsList(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = "books/book_details.html"
    model = Book
    context_object_name = "book"
    login_url = "account_login"
    permission_required = "books.special_status"

    def get_context_data(self, **kwargs):
        context = super(BookDetailsList, self).get_context_data()
        context["reviews"] = self.object.book_reviews.all()
        return context
