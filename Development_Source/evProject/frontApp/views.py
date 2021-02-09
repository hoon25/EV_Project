from django.shortcuts import render
from django.http import JsonResponse
from .models import *

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

def evgeolocation(request) :
    print('request evgeolocation - ')
    return render(request,'geolocation.html')

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
    for station in stations:
        list.append({
            'statnm' : station.statnm, 'addr': station.addr, 'lat' : station.lat, 'lng' : station.lng,
        })
    for a in list:
        print("check - ", a)
    return JsonResponse(list, safe = False)






