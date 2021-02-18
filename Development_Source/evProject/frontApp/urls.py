from django.contrib import admin
from django.urls import path, include
from frontApp import views

urlpatterns = [

    # 현재위치 기반 반경 2KM 이내에 존재하는 충전소 표시(정은경)
    path('mygps/', views.mygps, name='mygps'),
    path('evSearch/', views.evSearch, name='evSearch'),
    # 검색 기반 충전소 표시(최창훈)
    path('station/', views.station, name='station'),
    path('station_search/', views.stationSearch, name='stationSearch'),
    # 고속도로 길찾기 충전소 표시(최창훈)
    path('direction/', views.direction, name='diretion'),
    path('direction_search/', views.directionSearch, name='directionSearch'),
    # 충전소하나에 대한 페이지(최창훈)(개발예정)
    path('station_detail/', views.stationDetail, name='stationDetail'),
    # GPS 기반 컨텐츠 추천 (김보라)
    path('content_recommendation/', views.content_recommendation, name='content_recommendation'),
    path('content_recommendation_search/', views.content_recommendation_search, name='content_recommendation_search'),
    # 홈페이지 (서은상)
    path('index/', views.index, name='index'),
    path('login/', views.loginProc, name='login'),
    path('registerForm/', views.registerForm, name='registerForm'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('mypage/', views.mypage, name='mypage'),

    path('evgeolocation/', views.evgeolocation),
    path('station/', views.station, name = 'station'),
    path('station_search/', views.stationSearch, name = 'stationSearch'),


]

