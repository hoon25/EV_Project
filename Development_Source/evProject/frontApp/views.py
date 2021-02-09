from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *

# Create your views here.

# 현재 내위치 표시
def myloc(request) :
    print('request mylocation - ')
    return render(request,'geo_2.html')

def evloc(request) :
    print('request evloc - ')
    # return render(request,'naverMapApiEx1.html')
    # 35.5889950493
    # 129.3644580288
    # select * from EvStation where lat = ? and lng ?
    station = EvStation.objects.get(evsn=1)
    print('db station' , station)
    context = {'station' : station}
    return render(request,'naverMapApiEx1.html', context)

# def evloc(request) :
#     print('request evloc - ')
#     station = EvStation.objects.all()
#     print('db station' , station)
#     context = {'station' : station}
#     return render(request,'naverMapApiEx1.html', context)

# def locall(request) :
#     print('request locall - ')
#     station = EvStation.objects.all()
#     print('db station', station)
#     context = {'station': station}
#     return render(request, 'naverMapApiEx1.html', context)
    # return render(request, 'cluster.html')

# def locall(request) :
#     print('request locall - ')
#     return render(request, 'cluster.html')

def evclu(request) :
    print('request evclu - ')
    station = EvStation.objects.all()
    # print('db station' , station)
    # context = {'station' : station}
    # return render(request,'naverMapApiEx3.html', context)

    # station = EvStation.objects.get(evsn=1)
    print('db station', station)

    list = []
    cnt = 0
    for s in station :
        EvStation.lat = s.lat
        EvStation.lng = s.lng

        list.append({'lat' : s.lat , 'lng' : s.lng})
        cnt = cnt+1
        if cnt ==5 :
            break
    context = {'station': list}

    return render(request, 'naverMapApiEx3.html', context)
    # return render(request,'naverMapApiEx3.html')

