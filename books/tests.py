from django.contrib.auth.models import Permission
from django.http.request import HttpRequest
from django.test import TestCase
from .models import *


# Create your tests here.

class BookTest(TestCase):
    """Using setUpTestData often dramatically increases the speed of your tests because the initial data
is created once rather than each time for each unit test"""
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(title="Django for APIs", author='William S. Vincent', price="39.00")
        cls.user = get_user_model().objects.create_user(email="user@gmail.com",password="abcd1234",username="user")
        cls.review = Review.objects.create(user=cls.user,book=cls.book,review="Bien Joué")
        cls.perm = Permission.objects.get(codename="special_status")
    def test_book_info(self):
        self.assertEqual(f"{self.book.title}", "Django for APIs")
        self.assertEqual(f"{self.book.author}", "William S. Vincent")
        self.assertEqual(f"{self.book.price}", "39.00")
    def test_user_created(self):
        self.assertEqual(get_user_model().objects.get(email="user@gmail.com"),self.user)

    def test_books_listing_logged_user(self):
        logged = self.client.login(email="user@gmail.com",password="abcd1234")
        resp1 = self.client.get(reverse("books"))
        self.assertEqual(resp1.status_code, 200)
        self.assertTemplateUsed(resp1, "books/books_list.html")
        self.assertEqual(logged,True)

    def test_books_listing_unlogged_user(self):
        #self.client.logout()
        resp1 = self.client.get(reverse("books"))
        self.assertEqual(resp1.status_code, 302)


    def test_book_details(self):
        self.client.login(email="user@gmail.com",password="abcd1234")
        self.user.user_permissions.add(self.perm)
        no_resp = self.client.get("/books/123455")
        resp2 = self.client.get(self.book.get_absolute_url())
        self.assertEqual(resp2.status_code, 200)
        self.assertTemplateUsed(resp2, "books/book_details.html")
        self.assertEqual(no_resp.status_code, 404)
        self.assertContains(resp2,"Bien Joué")
