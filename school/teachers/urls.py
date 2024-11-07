from django.urls import path
from . import views

urlpatterns = [
    path('<teachersname>', views.allTeachersAll),
]
