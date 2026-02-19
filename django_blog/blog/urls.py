from django.urls import path
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', lambda request: render(request, 'blog/base.html'), name='home'),
    path('posts/', lambda request: render(request, 'blog/base.html'), name='posts'),
]
