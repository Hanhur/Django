from django.shortcuts import render
from .models import Book
from django.http import HttpResponseRedirect
from .forms import BookForm
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book(
                name = form.cleaned_data['book_name'],
                price = form.cleaned_data['book_price'],
            )
            book.save()
            return HttpResponseRedirect('/allbooks')
    else:
        form = BookForm()
        
        return render(request, 'bookapp/index.html', {
            'bookForm': form
        })

def all_books(request):
    books = Book.objects.all() # Získání všech knih z databáze
    return render(request, 'bookapp/allbooks.html', {
        'books': books,
    })

def delete_book(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    book.delete()
    return HttpResponseRedirect('/allbooks')

def edit_book(request, book_id):
    book = get_object_or_404(Book, id = book_id)

    if request.method == 'POST':
        book.name = request.POST['book-name']
        book.price = request.POST['book-price']
        book.save()
        return HttpResponseRedirect('/allbooks')
    
    return render(request, 'bookapp/editbook.html', {
        'book': book,
    })