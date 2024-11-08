from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:movienumber>', views.allMoviesNumber),
    path('<str:moviename>', views.allMoviesText, name = 'movie_url')
]
