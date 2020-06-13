"""Defines URL patterns for users"""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    #Login Page
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register, name='register'),
]
app_name = 'users'