from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home_page'),
    path('allbooks', views.all_books, name = 'all-books-url'),
    path('delete/<int:book_id>', views.delete_book, name = 'delete-book'),
    path('edit/<int:book_id>', views.edit_book, name = 'edit-book'),
]