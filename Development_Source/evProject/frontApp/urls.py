
from django.contrib import admin
from django.urls import path, include
from frontApp import views

urlpatterns = [
    path('mygps/', views.mygps,name='mygps'),
    path('evSearch/', views.evSearch, name='evSearch'),
    path('station/', views.station, name = 'station'),
    path('station_search/', views.stationSearch, name = 'stationSearch'),
    path('direction/', views.direction, name = 'diretion'),
    path('direction_search/', views.directionSearch, name='directionSearch'),
    path('station_detail/', views.stationDetail, name = 'stationDetail')
]