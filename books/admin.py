from django.contrib import admin
from .models import Publisher, Author, Book, BookCategory

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookCategory)
