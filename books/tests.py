from django.test import TestCase
from .models import *


# Create your tests here.

class BookTest(TestCase):

     def setup(self):
        self.book = Book.objects.create(title="Django for APIs", author='William S. Vincent', price=39.00)
        self.resp1 = self.client.get(reverse('books'))
        self.resp2 = self.client.get(reverse('book_details', args=str(self.book.id)))


     def book_info(self):
        self.assertEqual(self.book.title, "Django for APIs")
        self.assertEqual(self.book.author, "William S. Vincent")
        self.assertEqual(self.book.price, 39.00)

     def books_listing(self):
        self.assertEqual(self.resp1.status_code, 200)
        self.assertTemplateUsed(self.resp1, "books/books_list.html")

     def book_details(self):
        no_resp = self.client.get("/books/123455")
        self.assertEqual(self.resp2.status_code, 200)
        self.assertTemplateUsed(self.resp2, "books/book_details.html")
        self.assertEqual(no_resp.status_code, 404)
