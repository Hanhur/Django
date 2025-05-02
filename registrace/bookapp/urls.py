from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomLoginForm

urlpatterns = [
    path('', views.index, name = 'homepage-url'),
    path('register', views.register, name = 'register-url'),
    path('login', auth_views.LoginView.as_view(template_name = 'bookapp/login.html', authentication_form = CustomLoginForm), name = 'login-url'),
    path('logout', auth_views.LogoutView.as_view(), name = 'logout-url'),
    path('dashboard', views.dashboard, name = 'dashboard-url'),
    path('protected-page', views.protected_page, name = 'protected-page-url'),
]