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


class Sspbank(models.Model):
    bankid = models.IntegerField(primary_key=True)
    bankname = models.CharField(max_length=50)
    bankcode = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'sspbank'


class Sspcardtype(models.Model):
    cardtypeid = models.IntegerField(primary_key=True)
    cardtype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sspcardtype'


class Sspcity(models.Model):
    cityid = models.IntegerField(primary_key=True)
    provinceid = models.ForeignKey('Sspprovince', db_column='provinceid')
    city = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sspcity'


class Sspjob(models.Model):
    jobid = models.IntegerField(primary_key=True)
    job = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sspjob'


class Sspmerchanttype3(models.Model):
    merchanttypeid = models.IntegerField(primary_key=True)
    merchanttype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sspmerchanttype'
        verbose_name="data3"


class Sspnationality(models.Model):
    nationalityid = models.IntegerField(primary_key=True)
    nationality = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sspnationality'


class Sspprovince(models.Model):
    provinceid = models.IntegerField(primary_key=True)
    province = models.CharField(max_length=40)
    stateid = models.ForeignKey('Sspstate', db_column='stateid')

    class Meta:
        managed = False
        db_table = 'sspprovince'



class Sspsex(models.Model):
    sexid = models.IntegerField(primary_key=True)
    sex = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'sspsex'


class Sspstate(models.Model):
    stateid = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'sspstate'
