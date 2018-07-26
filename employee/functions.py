# -*- coding: utf-8 -*-

from django.http import (
    HttpResponse,
)
import string
import random
import urllib2, urllib
import datetime
import binascii
import logging
logger = logging.getLogger(__name__)
import json
import re
from employee.sql_function import (
    sql_Proc2,
)
    
def check_array_null(listCheck, *args):
    listCheck = listCheck
    for arg in args:
     try:
       listCheck[arg] = str(listCheck[arg])
     except:
       listCheck[arg] = None
    return listCheck

def check_array_null_1(listCheck, args):
    listCheck = listCheck
    for arg in args:
     try:
       listCheck[arg] = str(listCheck[arg])
     except:
       listCheck[arg] = None
    return listCheck



def getkeyfromlistdict5(keydict, value):
    list_dict = dict()
    list_dict = keydict
    for k, v in list_dict.items():
      if list_dict in v:
        return str(k)
        break
    return 'data5'

def api_post_sp5(sp_database, *args, **kwargs):
    import warnings
    warnings.filterwarnings("ignore", "No data .*")
    sql = sql_Proc2(getkeyfromlistdict5(m_sp_database, sp_database), sp_database, args)
    data_sql = [h for h in sql][0]
    len_data = len(data_sql)
    isList = False
    if data_sql and len_data != 0:
        if len_data > 1:
            isList = True
            data = list()
        key = list()
        for i, j in kwargs.iteritems():
            if not i[:4] == "var_":
                    key.append(i)
        key = tuple(key)
        for usr in data_sql:
                result_usr = check_array_null_1(usr, key)
                for i, j in kwargs.iteritems():

                    if i[:4] == "var_":
                        result_usr[i[4:]] = str(j)
                if isList:
                    data.append(result_usr)
                else:
                    data = result_usr
    else:
        data = {
            'status' : 0,
            'message' : 'zero rows'
        }
    return data


def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")
