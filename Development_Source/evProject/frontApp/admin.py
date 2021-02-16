from django.contrib import admin
from frontApp.models import EvCodeInf,EvInfo,EvRealTime,EvReview,EvStation,EvStationChgertype,EvStationStatus,MyEvList,RegionCode,UserCar,UserInfo


# Register your models here.
admin.site.register(EvCodeInf)
admin.site.register(EvInfo)
admin.site.register(EvRealTime)
admin.site.register(EvReview)
admin.site.register(EvStation)
admin.site.register(EvStationChgertype)
admin.site.register(EvStationStatus)
admin.site.register(MyEvList)
admin.site.register(RegionCode)
admin.site.register(UserCar)
admin.site.register(UserInfo)
