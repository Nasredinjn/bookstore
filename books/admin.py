from django.contrib import admin
from .models import *


# Register your models here.
class ReviewInline(admin.TabularInline): # to add the option to add / change records of this model from another model which's Book
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    list_display = ["title", "author", "price"]


admin.site.register(Book, BookAdmin)
