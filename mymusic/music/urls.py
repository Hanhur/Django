from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.music_detail, name='song_detail'),
    # song_detail = http://127.0.0.1:8000/<int:id>
]