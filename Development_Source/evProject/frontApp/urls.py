
from django.contrib import admin
from django.urls import path, include
from frontApp import views


# urlpatterns = [
#     path('index/', views.index),
#     path('ex1/', views.naverMapEx1),
#     path('ex2/', views.naverMapEx2),
#     path('ex3/', views.naverMapEx3),
# ]

urlpatterns = [
    path('evgeolocation/', views.evgeolocation),
    path('station/', views.station, name = 'station'),
    path('station_search/', views.stationSearch, name = 'stationSearch'),
    path('direction/', views.direction, name = 'diretion'),
    path('direction_search/', views.directionSearch, name='directionSearch'),
    path('station_detail/', views.stationDetail, name = 'stationDetail')
]