# Create your models here.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EvCodeInf(models.Model):
    codeid = models.CharField(db_column='codeId', primary_key=True, max_length=5)  # Field name made lowercase.
    codename = models.CharField(db_column='codeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codetype = models.CharField(db_column='codeType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    useyn = models.CharField(db_column='useYN', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ev_code_inf'


class EvInfo(models.Model):
    evsn = models.BigAutoField(db_column='evSn', primary_key=True)  # Field name made lowercase.
    statid = models.CharField(db_column='statId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    statnm = models.CharField(db_column='statNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chgerid = models.CharField(db_column='chgerId', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chgertype = models.CharField(db_column='chgerType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(max_length=150, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    usetime = models.CharField(db_column='useTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    busiid = models.CharField(db_column='busiId', max_length=2, blank=True, null=True)  # Field name made lowercase.
    businm = models.CharField(db_column='busiNm', max_length=50, blank=True, null=True)  # Field name made lowercase.
    busicall = models.CharField(db_column='busiCall', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(max_length=1, blank=True, null=True)
    statupddt = models.DateTimeField(db_column='statUpdDt', blank=True, null=True)  # Field name made lowercase.
    powertype = models.CharField(db_column='powerType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zcode = models.CharField(max_length=2, blank=True, null=True)
    parkingfree = models.CharField(db_column='parkingFree', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ev_info'


class EvRealTime(models.Model):
    evsn = models.BigIntegerField(db_column='evSn', primary_key=True)  # Field name made lowercase.
    congestion = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ev_real_time'


class EvReview(models.Model):
    reviewsn = models.IntegerField(db_column='reviewSn', primary_key=True)  # Field name made lowercase.
    evsn = models.IntegerField(db_column='evSn', blank=True, null=True)  # Field name made lowercase.
    star = models.IntegerField(blank=True, null=True)
    review = models.CharField(max_length=200, blank=True, null=True)
    userid = models.CharField(db_column='userId', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ev_review'


class EvStation(models.Model):
    evsn = models.BigAutoField(db_column='evSn', primary_key=True)  # Field name made lowercase.
    statid = models.CharField(db_column='statId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    statnm = models.CharField(db_column='statNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(max_length=150, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    usetime = models.CharField(db_column='useTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    busiid = models.CharField(db_column='busiId', max_length=2, blank=True, null=True)  # Field name made lowercase.
    businm = models.CharField(db_column='busiNm', max_length=50, blank=True, null=True)  # Field name made lowercase.
    busicall = models.CharField(db_column='busiCall', max_length=20, blank=True, null=True)  # Field name made lowercase.
    statupddt = models.DateTimeField(db_column='statUpdDt', blank=True, null=True)  # Field name made lowercase.
    powertype = models.CharField(db_column='powerType', max_length=4, blank=True, null=True)  # Field name made lowercase.
    zcode = models.CharField(max_length=2, blank=True, null=True)
    parkingfree = models.CharField(db_column='parkingFree', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ev_station'


class EvStationChgertype(models.Model):
    evsn = models.BigIntegerField(db_column='evSn')  # Field name made lowercase.
    statid = models.CharField(db_column='statId', max_length=8)  # Field name made lowercase.
    chgerid = models.CharField(db_column='chgerId', max_length=2)  # Field name made lowercase.
    chgertype = models.CharField(db_column='chgerType', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ev_station_chgertype'


class EvStationStatus(models.Model):
    evsn = models.BigIntegerField(db_column='evSn', primary_key=True)  # Field name made lowercase.
    statid = models.CharField(db_column='statId', max_length=8)  # Field name made lowercase.
    chgerid = models.CharField(db_column='chgerId', max_length=2)  # Field name made lowercase.
    stat = models.CharField(max_length=5)
    upddt = models.DateTimeField(db_column='updDt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ev_station_status'
        unique_together = (('evsn', 'chgerid'),)


class MyEvList(models.Model):
    evsn = models.BigIntegerField(db_column='evSn', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userId', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'my_ev_list'
        unique_together = (('evsn', 'userid'),)


class RegionCode(models.Model):
    zcode = models.IntegerField(primary_key=True)
    region = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region_code'


class UserCar(models.Model):
    carnum = models.CharField(db_column='carNum', primary_key=True, max_length=45)  # Field name made lowercase.
    cartype = models.CharField(db_column='carType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userId', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_car'


class UserInfo(models.Model):
    userid = models.CharField(db_column='userId', primary_key=True, max_length=45)  # Field name made lowercase.
    nicknm = models.CharField(db_column='nickNm', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usernm = models.CharField(db_column='userNm', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pwd = models.CharField(max_length=45, blank=True, null=True)
    phonenum = models.CharField(db_column='phoneNum', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_info'