from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:dayinweek_number>', views.dayNumber),
    path('<str:dayinweek_string>', views.dayText, name = 'days_tasks'),
]
