from django import views
from django.contrib import admin
from django.urls import path, include
from homepage import views


urlpatterns = [
    path('Main', views.Main, name = "Main"),
    path('Profile', views.Profile, name = "Profile"),
    path('Points', views.Points, name = "Points"),
    path('Task', views.Task, name= "Task"),
    path('Logout', views.Logout, name= "Logout"),
]
