from django.contrib import admin
from frontApp.models import CarList, EvCodeInf,EvInfo,EvReview,EvStation,EvStationChgertype,EvStationInoutStat,EvStationStatus,EvStationStatusStat,MyEvList,RegionCode,UserCar,UserInfo


# Register your models here.
admin.site.register(CarList)
admin.site.register(EvCodeInf)
admin.site.register(EvInfo)
admin.site.register(EvReview)
admin.site.register(EvStation)
admin.site.register(EvStationChgertype)
admin.site.register(EvStationInoutStat)
admin.site.register(EvStationStatus)
admin.site.register(EvStationStatusStat)
admin.site.register(MyEvList)
admin.site.register(RegionCode)
admin.site.register(UserCar)
admin.site.register(UserInfo)

