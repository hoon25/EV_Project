
from django.contrib import admin
from django.urls import path, include
from frontApp import views

urlpatterns = [
    path('home/', views.home,name='home'),
    # 현재위치 기반 반경 2KM 이내에 존재하는 충전소 표시(정은경)
    path('mygps/', views.mygps,name='mygps'),
    path('evSearch/', views.evSearch, name='evSearch'),
    #
    path('station/', views.station, name = 'station'),
    path('station_search/', views.stationSearch, name = 'stationSearch'),
    path('direction/', views.direction, name = 'diretion'),
    path('direction_search/', views.directionSearch, name='directionSearch'),
    path('station_detail/', views.stationDetail, name = 'stationDetail'),
    # GPS 기반 컨텐츠 추천 (김보라)
    path('content_recommendation/', views.content_recommendation, name = 'content_recommendation'),
    #홈페이지 (서은상)
    path('index/', views.index , name='index'),
    path('login/' , views.loginProc, name='login'),
    path('registerForm/', views.registerForm, name='registerForm'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
]