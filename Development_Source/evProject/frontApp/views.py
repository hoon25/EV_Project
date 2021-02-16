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


def evSearch(request) :
    if request.method == 'POST':
        user_lat = request.POST['lat']
        user_lng = request.POST['lng']
    try:
        cursor = connection.cursor()
        # strSql = "SELECT DISTINCT statNm,addr,lat,lng,useTime,powerType,stat,chgerType,codeName,\
        #             (6371*acos(cos(radians("+user_lat+"))*cos(radians(lat))*cos(radians(lng)-radians("+user_lng+"))+sin(radians("+user_lat+"))*sin(radians(lat))))AS distance \
        #             FROM ev_station E \
        #             JOIN ev_station_status S ON(E.evsn = S.evsn) \
        #             JOIN ev_station_chgertype C ON(E.evsn = C.evsn) \
        #             JOIN ev_code_inf I ON(S.stat = I.codeId) \
        #             HAVING distance <= 2 \
        #             ORDER BY distance"

        strSql = "select evst.statNm,evst.addr,evst.lat,evst.lng,evst.useTime,evst.busiCall,descInfo,congestion, \
                (6371*acos(cos(radians("+user_lat+"))*cos(radians(evst.lat))*cos(radians(evst.lng)-radians("+user_lng+"))+sin(radians("+user_lat+"))*sin(radians(evst.lat))))AS distance \
                from ev_station evst \
                join ev_real_time evtm on(evst.evsn=evtm.evsn),\
                (select c.evSn, group_concat(des SEPARATOR '\n') as descInfo \
                from (select a.evSn, a.chgerId, concat('기기 번호 : ', a.chgerId , ' ( 상태 : ' , (select codeName from ev.ev_code_inf where codeId = a.stat) , ', 충전타입 : ' \
                      ,GROUP_CONCAT((select codeName from ev.ev_code_inf where codeId = b.chgerType) SEPARATOR ','),')') as des \
                from ev_station_status a,ev_station_chgertype b \
                where a.evSn = b.evSn \
                group by a.evSn, a.chgerId) c \
                group by c.evSn) info \
                where evst.evSn = info.evSn \
                HAVING distance <= 2 \
                ORDER BY distance;"

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
                   'useTime' : station[4],
                   'busiCall' : station[5],
                   'descInfo' : station[6],
                   'congestion' : station[7],
                   'distance': station[8]}
            list.append(row)
            if station[7]<0.5 :
                context = {'congestion': '한산'}
                print('한산')
            elif station[7]<0.99 :
                context = {'congestion': '보통'}
                print('보통')
            else:
                context = {'congestion': '복잡'}
                print('복잡')
            cnt = cnt + 1
            if cnt == 5 :
              break
        for a in list:
            print("check - ", a)
    except :
        connection.rollback()
        print('Failed selecting in stations')
    return JsonResponse(list, safe=False)



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
        if cnt == 5 :
            break
    for a in list:
        print("check - ", a)
    return JsonResponse(list, safe = False)

