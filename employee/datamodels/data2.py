# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Sspadmin(models.Model):
    adminid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.TextField()
    password = models.TextField()
    loginstatus = models.IntegerField()
    cryptoid = models.IntegerField()
    photo = models.CharField(max_length=255, blank=True)
    idscan = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'sspadmin'


class Sspclient2(models.Model):
    clientid = models.CharField(primary_key=True, max_length=20)
    imei = models.TextField()
    securitychar = models.TextField()
    password1 = models.TextField()
    securitycharexp = models.DateTimeField(blank=True, null=True)
    imeitemp = models.TextField()
    client_status = models.CharField(max_length=10)
    login_attempt = models.IntegerField()
    cryptoid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sspclient'
        verbose_name="data2"


class Sspclientaccess(models.Model):
    clientaccessid = models.IntegerField(primary_key=True)
    clientid = models.CharField(max_length=255, blank=True)
    imei = models.CharField(max_length=255)
    session_key = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sspclientaccess'


class Sspclientqa(models.Model):
    questionid = models.IntegerField(primary_key=True)
    clientid = models.ForeignKey(Sspclient2, db_column='clientid')
    questionnumber = models.IntegerField()
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspclientqa'


class Sspemployee2(models.Model):
    employeeid = models.IntegerField(primary_key=True)
    username = models.TextField()
    password = models.TextField()
    cryptoid = models.IntegerField()
    photo = models.CharField(max_length=255, blank=True)
    idscan = models.CharField(max_length=255, blank=True)
    employeestatus = models.CharField(max_length=8, blank=True)

    class Meta:
        managed = False
        db_table = 'sspemployee'
        verbose_name="data2"


class Sspmerchant2(models.Model):
    merchantid = models.CharField(primary_key=True, max_length=20)
    username = models.TextField()
    password = models.TextField()
    merchantstatus = models.CharField(max_length=16)
    cryptoid = models.IntegerField()
    idcardscan = models.TextField()
    npwpscan = models.TextField()
    businesslicensescan = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspmerchant'
        verbose_name="data2"


class Sspmerchantqa(models.Model):
    merchantqaid = models.IntegerField(primary_key=True)
    merchantid = models.ForeignKey(Sspmerchant2, db_column='merchantid')
    questionnumber = models.IntegerField()
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspmerchantqa'


class Ssppos(models.Model):
    posid = models.TextField(primary_key=True)
    userid = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ssppos'


class Ssptransactiontoken(models.Model):
    transtokenid = models.IntegerField(primary_key=True)
    transactionid = models.IntegerField()
    token = models.TextField()

    class Meta:
        managed = False
        db_table = 'ssptransactiontoken'
