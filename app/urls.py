from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('', views.signuppage,name='signuppage'),
    path('loginpage', views.loginpage,name='loginpage'),
    path('homepage', views.homepage,name='homepage')
]