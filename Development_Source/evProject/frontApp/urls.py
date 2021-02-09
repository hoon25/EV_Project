
from django.contrib import admin
from django.urls import path, include
from frontApp import views



urlpatterns = [
    path('myloc/', views.myloc),
    # path('evloc/', views.evloc),
    # path('locall/', views.locall),
    path('evclu/', views.evclu),

]