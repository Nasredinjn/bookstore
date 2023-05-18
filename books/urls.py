from django.urls import path
from .views import *
urlpatterns = [
    path('',BookListView.as_view(),name='books'),
    path('<uuid:pk>/',BookDetailsList.as_view(),name="book_details"),
    path("search/", SearchResultsListView.as_view(),name="search")
]