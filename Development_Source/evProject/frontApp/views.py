from django.shortcuts import render
from django.http import JsonResponse

from .models import *
from django.db import connection


from frontApp.getApi.directionApi import getDirectionApi # 네이버지도 길찾기
from frontApp.getApi.geocodeApi import getGeocode # 네이버 주소 기반 좌표반환



def mygps(request) :
    print('request mygps - ')
    return render(request,'geo_2.html')
def evSearch(request) :
    if request.method == 'POST':
        user_lat = request.POST['lat']
        user_lng = request.POST['lng']
    try:
        cursor = connection.cursor()
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
        # cnt = 0
        for station in stations:
            conlevel = ""
            if station[7]<0.5 :
                conlevel = 'green-dot.png'
                print(conlevel)
            elif station[7]<0.99 :
                conlevel = 'yellow-dot.png'
                print(conlevel)
            else:
                conlevel = 'red-dot.png'
                print(conlevel)
            row = {'statNm': station[0],
                   'addr': station[1],
                   'lat': station[2],
                   'lng': station[3],
                   'useTime': station[4],
                   'busiCall': station[5],
                   'descInfo': station[6],
                   'congestion': station[7],
                   'distance': station[8] ,
                   'conlevel': conlevel}
            list.append(row)
            # cnt = cnt + 1
            # if cnt == 5 :
            #   break
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


def station(request):
    print("check station load")
    return render(request, 'naversearch.html')

def stationSearch(request):
    type = request.POST['type']
    keyword = request.POST['keyword']
    print("Check Post -", type, keyword)

    if type == 'statnm':
        try:
            cursor = connection.cursor()
            strSql = "select evst.statNm,evst.addr,evst.lat,evst.lng,evst.useTime,evst.busicall, info.descInfo " \
                     "from ev.ev_station evst,(select c.evSn, group_concat(des SEPARATOR '\n') as descInfo " \
                     "from (select a.evSn, a.chgerId, concat('기기 번호 :', a.chgerId , ' ( 상태 : ' , (select codeName from ev_code_inf where codeId = a.stat) , ', 충전타입 : ' , GROUP_CONCAT((select codeName from ev_code_inf where codeId = b.chgerType) SEPARATOR ','),')') as des " \
                     "from ev.ev_station_status a, ev.ev_station_chgertype b " \
                     "where	a.evSn = b.evSn group by a.evSn, a.chgerId) c group by c.evSn) info " \
                     "where evst.evSn = info.evSn and evst.statNm Like '%"+keyword+"%';"

            result = cursor.execute(strSql)
            stations = cursor.fetchall()
            print('stations - ', stations)

            connection.commit()
            connection.close()

        except:
            connection.rollback()
            print('Failed selecting in stations')


    elif type == 'addr':
        try:
            cursor = connection.cursor()
            strSql = "select evst.statNm,evst.addr,evst.lat,evst.lng,evst.useTime,evst.busicall, info.descInfo " \
                     "from ev.ev_station evst,(select c.evSn, group_concat(des SEPARATOR '\n') as descInfo " \
                     "from (select a.evSn, a.chgerId, concat('기기 번호 :', a.chgerId , ' ( 상태 : ' , (select codeName from ev_code_inf where codeId = a.stat) , ', 충전타입 : ' , GROUP_CONCAT((select codeName from ev_code_inf where codeId = b.chgerType) SEPARATOR ','),')') as des " \
                     "from ev.ev_station_status a, ev.ev_station_chgertype b " \
                     "where	a.evSn = b.evSn group by a.evSn, a.chgerId) c group by c.evSn) info " \
                     "where evst.evSn = info.evSn and evst.addr Like '%"+keyword+"%';"

            result = cursor.execute(strSql)
            stations = cursor.fetchall()
            print('stations - ', stations)

            connection.commit()
            connection.close()
        except:
            connection.rollback()
            print('Failed selecting in stations')
    list = []
    cnt = 0
    for station in stations:
        row = {'statnm': station[0],
               'addr': station[1],
               'lat': station[2],
               'lng': station[3],
               'useTime': station[4],
               'busicall': station[5],
               'info': station[6]}
        list.append(row)
        cnt += 1
        if cnt == 100:
            break
    for a in list:
        print("check - ", a)
    print(len(list))

    return JsonResponse(list, safe=False)



def direction(request):
    print("check direction load")
    return render(request, 'naverdirection.html')

def directionSearch(request):
    start = request.POST['start']
    goal = request.POST['goal']


    print("Check Post -", start, goal)
    startGeo = getGeocode(start)
    goalGeo = getGeocode(goal)
    startLocation = startGeo[2] + "," + startGeo[3]
    goalLocation = goalGeo[2] + "," + goalGeo[3]
    print(startLocation)
    print(goalLocation)

    directionDataList = getDirectionApi(startLocation,goalLocation)
    # print(directionDataList)


    list = []
    for directionData in directionDataList:
        latitude = str(directionData[1])
        longtitude = str(directionData[0])
        # print(latitude)
        # print(longtitude)

        try:
            cursor = connection.cursor()
            strSql = "select evst.statNm,evst.addr,evst.lat,evst.lng,evst.busicall, evst.useTime,(6371*acos(cos(radians("+latitude+"))*cos(radians(evst.lat))*cos(radians(evst.lng)-radians("+longtitude+"))+sin(radians("+latitude+"))*sin(radians(evst.lat))))AS distance, info.descInfo from ev.ev_station evst,(select c.evSn, group_concat(des SEPARATOR '\n') as descInfo from (select	a.evSn, a.chgerId, concat('기기 번호 :', a.chgerId , ' ( 상태 : ' , (select codeName from ev.ev_code_inf where codeId = a.stat) , ', 충전타입 : ', GROUP_CONCAT((select codeName from ev.ev_code_inf where codeId = b.chgerType) SEPARATOR ','),')') as des from ev.ev_station_status a, ev.ev_station_chgertype b where a.evSn = b.evSn group by a.evSn, a.chgerId) c group by c.evSn) info where evst.evSn = info.evSn HAVING distance <= 1 ORDER BY distance;"

            result = cursor.execute(strSql)
            stations = cursor.fetchall()
            # print('stations - ', stations)

            connection.commit()
            connection.close()


            cnt = 0
            for station in stations:
                row = {'statnm': station[0],
                       'addr': station[1],
                       'lat': station[2],
                       'lng': station[3],
                       'useTime': station[4],
                       'busicall': station[5],
                       'info': station[7]}
                list.append(row)
                cnt += 1
                if cnt == 3:
                    break
        except:
            connection.rollback()
            print('Failed selecting in stations')

    # for a in list:
    #     print("check - ", a)
    # print(len(list))


    return JsonResponse(list, safe = False)


def stationDetail(request):
    print("stationDetail load")

    return render(request, 'stationDetail.html')

def content_recommendation(request):
    return render(request, 'ContentRecommendation.html')


