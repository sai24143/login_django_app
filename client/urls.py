from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.login, name='login' ),
    path('home/', views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('main/',views.main, name='main'),
    path('signout/',views.signout, name='signout'),
    
]
