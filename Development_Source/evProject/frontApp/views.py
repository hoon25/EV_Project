from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.db import connection
import math
from haversine import haversine, Unit
from django.db.models import Q

from django.core import serializers
from django.http import HttpResponse

# Create your views here.

# select * from table ;
# -> modelName.objects.all()

# select * from table where id = xxxx and pwd = xxxx;
# -> modelName.objects.get(id = xxxx, pwd = xxxx)
# -> modelName.objects.filter(id = xxxx, pwd = xxxx)

# select * from table where id = xxxx or pwd = xxxx;
# -> modelName.objects.filter(Q(id = xxxx) | Q(pwd = xxxx))

# select * from table where subject like '%공지%'
# -> modelName.objects.filter(subject__icontains = '공지')
# select * from table where subject like '공지%'
# -> modelName.objects.filter(subject__startswith = '공지')
# select * from table where subject like '%공지'
# -> modelName.objects.filter(subject__endswith = '공지')

# insert into table values()
# model(attr=value, attr = value)
# model.save()

# delete * from tableName where id = xxxx
# -> modelName.objects.get(id=xxx).delete()

# update tableName set attr = value where id = xxxxx
# obj = modelName.objects.get(id=xxxxx)
# obj.attr = value
# obj.save() -- commit

def mygps(request) :
    print('request mygps - ')
    return render(request,'geo_2.html')
    # return render(request, 'naverMapApiEx2.html')

def evSearch(request) :
    if request.method == 'POST':
        type = request.POST['type']
        distance = request.POST['distance']
        # stations = EvStation.objects.get(statnm=type)
    try:
        cursor = connection.cursor()
        strSql = 'SELECT statNm,addr,lat,lng, \
                    (6371*acos(cos(radians(37.5766831))*cos(radians(lat))*cos(radians(lng)-radians(126.8978620))+sin(radians(37.5766831))*sin(radians(lat))))AS distance \
                    FROM ev_station \
                    HAVING distance <= 2 \
                    ORDER BY distance'

        result = cursor.execute(strSql)
        stations = cursor.fetchall()
        print('stations - ', stations)

        connection.commit()
        connection.close()

        list = []
        cnt = 0
        for station in stations:
            row = {'statNm': station[0],
                   'addr': station[1],
                   'lat': station[2],
                   'lng': station[3],
                   'distance': station[4]}
            list.append(row)
            cnt = cnt + 1
            if cnt == 5 :
              break
        for a in list:
            print("check - ", a)
    except :
        connection.rollback()
        print('Failed selecting in stations')
    return JsonResponse(list, safe=False)



# def evSearch(request) :
#     if request.method == 'POST' :
#         lat = request.POST['lat'],
#         lng = request.POST['lng']
#         print('request evSearch -- ' , lat, lng)
#         # stations = EvStation.objects.get(statnm=type)
#         stations01 = EvStation.objects.filter(lat=lat)
#         stations02 = EvStation.objects.filter(lng=lng)
#         stations = [stations01, stations02]
#         print('stations', stations)
#         list = []
#         cnt = 0
#         for station in stations:
#             list.append({
#                 'statnm': station.statnm, 'addr': station.addr, 'lat': station.lat, 'lng': station.lng
#             })
#             cnt = cnt + 1
#             if cnt == 5:
#                 break
#         for a in list:
#             print("check - ", a)
#         return JsonResponse(list, safe=False)


def station(request):
    print("check station load")
    return render(request, 'naversearch.html')

def stationSearch(request):
    type = request.POST['type']
    keyword = request.POST['keyword']
    # print("Check Post -", type, keyword)

    if type == 'statnm':
        stations = EvStation.objects.filter(statnm__icontains = keyword)
    elif type == 'addr':
        stations = EvStation.objects.filter(addr__icontains = keyword)

    list = []
    cnt = 0
    for station in stations:
        list.append({
            'statnm' : station.statnm, 'addr': station.addr, 'lat' : station.lat, 'lng' : station.lng,
        })
        cnt = cnt + 1
        if cnt ==5 :
            break
    for a in list:
        print("check - ", a)
    return JsonResponse(list, safe = False)




# def evSearch(request):
#     try:
#         lat = request.POST['lat']
#         lng = request.POST['lng']
#         position = (lat, lng)
#         condition = (
#             Q(latitude__range  = (lat - 0.01, lat + 0.01)) | Q(longitude__range = (lng - 0.015, lng + 0.015))
#         )
#
#         convenience_infos = (
#             EvStation.objects.filter(condition)
#         )
#         near_convenience_infos = [info for info in convenience_infos
#                                   if haversine(position, (info.latitude, info.longitude)) <= 2]
#
# return JsonResponse(near_convenience_infos, safe = False)




# def latLng(request):
#     if request.method == 'POST' :
#         position = EvStation.objects.all()
#         position = request.POST['position']
#         print('request position - ', position)
#         list = []
#         cnt = 0
#         for latlng in position :
#             EvStation.lat = latlng.lat
#             EvStation.lng = latlng.lng
#             list.append({'lat' : latlng.lat,
#                          'lng' : latlng.lng})
#             cnt += 1
#             if cnt == 5 :
#                 break
#         context = {'position' : list}
#         return JsonResponse(list, safe=False)






