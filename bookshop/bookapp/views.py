from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    if request.method == 'POST':
        book_name = request.POST['book-name']
        book_price = request.POST['book-price']
        # print(book_name, book_price)

        # Uložení dat do databáze
        Book.objects.create(
            name = book_name,
            price = book_price
        )
        print('Data uložena')
        
    return render(request, 'bookapp/index.html')