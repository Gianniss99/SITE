from django.shortcuts import render, get_object_or_404
from .models import Book
from datetime import datetime


def book_list(request):
    current_year = datetime.now().year
    books = Book.objects.filter(publish_year__lte=current_year).order_by('-publish_year')
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def book_list(request):
    books = Book.objects.all().order_by('-publish_year')
    cat_id = request.GET.get('cat')
    pub_id = request.GET.get('pub')
    auth_id = request.GET.get('auth')

    if cat_id:
        books = books.filter(category_id=cat_id)
    if pub_id:
        books = books.filter(publisher_id=pub_id)
    if auth_id:
        books = books.filter(author_id=auth_id)

    return render(request, 'books/book_list.html', {'books': books})
