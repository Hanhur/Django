from django.urls import path
from . import views

urlpatterns = [
    path('', views.startingPage, name = 'starting_page'),
    path('movies', views.allMoviesPage, name = 'movies_page'),
]
