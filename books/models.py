import uuid

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.urls import reverse


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        permissions = [
            ("special_status", "can read all books")
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_details", args=[str(self.id)])

    @property
    def book_cover(self):
        if self.cover:
            return getattr(self.cover, "url", None)
        return None


class Review(models.Model):
    book = models.ForeignKey(
        "Book",
        related_name="book_reviews",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        get_user_model(),
        related_name="user_reviews",
        on_delete=models.CASCADE
    )
    review = models.CharField(max_length=300)

    def __str__(self):
        return self.review
