
from django.contrib import admin
from django.urls import path, include
from frontApp import views


urlpatterns = [
    path('index/', views.index),
    path('ex1/', views.naverMapEx1),
    path('ex2/', views.naverMapEx2),
    path('ex3/', views.naverMapEx3),
]
