
from django.contrib import admin
from django.urls import path, include
from frontApp import views

urlpatterns = [
    path('mygps/', views.mygps,name='mygps'),
    path('evSearch/', views.evSearch, name='evSearch'),
    # path('evSearch02/', views.evSearch02, name='evSearch02'),
    path('station/', views.station, name = 'station'),
    path('station_search/', views.stationSearch, name = 'stationSearch'),

]