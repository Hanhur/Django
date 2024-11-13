from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name = 'starting-page'),
    path('all-movies/', views.all_movies, name = 'all-movies-page'),
    path('all-movies/<slug:slug>', views.movie_detail, name = 'movie-detail-page'),
]
