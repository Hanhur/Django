from django.shortcuts import render
from books.models import Book
from django.db.models import Q

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {
        'all_books' : books,
    })