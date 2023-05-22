from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

class BookListView(LoginRequiredMixin, ListView):
    template_name = "books/books_list.html"
    model = Book
    context_object_name = "books"
    login_url = "account_login"
    def get_queryset(self):
        return Book.objects.all()
        #.only() is used for optimization because instead of queryin all cols we just qury the cols that we needwhich's title here
class BookDetailsList(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = "books/book_details.html"
    model = Book
    context_object_name = "book"
    login_url = "account_login"
    permission_required = "books.special_status"
    #queryset =  Book.objects.filter(.prefetch_related("book_reviews__user")
    def get_context_data(self, **kwargs):
        context = super(BookDetailsList, self).get_context_data()
        context["reviews"] = self.object.book_reviews.all()
        return context
    def get_queryset(self):
        #queryset = super().get_queryset()
        book_id = self.kwargs['pk']
        queryset = Book.objects.filter(id=book_id).prefetch_related("book_reviews__user")

        return queryset


class SearchResultsListView(ListView):
    model = Book
    template_name = "books/search_result.html"
    context_object_name = "search_result"
    def get_queryset(self):
        searched_book = self.request.GET.get("q",None)
        if searched_book:
            return Book.objects.filter(
              Q(title__icontains=searched_book)
            )