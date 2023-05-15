from django.test import TestCase
from .models import *


# Create your tests here.

class BookTest(TestCase):
    """Using setUpTestData often dramatically increases the speed of your tests because the initial data
is created once rather than each time for each unit test"""
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(title="Django for APIs", author='William S. Vincent', price="39.00")

    def test_book_info(self):
        self.assertEqual(f"{self.book.title}", "Django for APIs")
        self.assertEqual(f"{self.book.author}", "William S. Vincent")
        self.assertEqual(f"{self.book.price}", "39.00")

    def test_books_listing(self):
        resp1 = self.client.get(reverse("books"))
        self.assertEqual(resp1.status_code, 200)
        self.assertTemplateUsed(resp1, "books/books_list.html")

    def test_book_details(self):
        no_resp = self.client.get("/books/123455")
        resp2 = self.client.get(self.book.get_absolute_url())
        self.assertEqual(resp2.status_code, 200)
        self.assertTemplateUsed(resp2, "books/book_details.html")
        self.assertEqual(no_resp.status_code, 404)
