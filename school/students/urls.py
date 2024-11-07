# URLS v aplikaci students
from django.urls import path
from . import views

urlpatterns = [
    path('<studentsname>', views.allstudentsinfo),
    # path('david', views.davidStudents),
    # path('harry', views.harryStudents),
    # path('hermiona', views.hermionaStudents),
    # path('ron', views.ronStudents),
]
