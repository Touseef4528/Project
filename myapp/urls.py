from django.contrib import admin
from django.urls import path, include
from myapp import views 

urlpatterns = [

    path('index', views.index, name="index"),
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('new/', views.new, name="new"),

    path('logout/', views.logout, name="logout"),
    path('get/', views.getsession, name="getsession"),
    


]