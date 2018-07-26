from itertools import *
from django.db import connections, transaction
import logging

class sql_Query:

    django = "data"
    data = "data1"



logger = logging.getLogger(__name__)
def sql_Proc(db, query_string, *query_args):
   try:
       cursor = connections[db].cursor()
       cursor.callproc(query_string, query_args)
       col_names = [desc[0] for desc in cursor.description]
       value = []
       while True:
           row = cursor.fetchone()
           if row is None:
               break
           row_dict = dict(izip(col_names, row))
           value.append(row_dict)
       yield value
   except:
       value = [{'status':0, 'message':'Error SQL Process'}]
       yield value
       return
   finally:
       cursor.close()
       return

def sql_Proc2(db, query_string, *query_args):
   try:
       data = query_args[0]
       #logger.info(data)
       cursor = connections[db].cursor()
       cursor.callproc(query_string, data)
       col_names = [desc[0] for desc in cursor.description]
       value = []
       while True:
           row = cursor.fetchone()
           if row is None:
               break
           row_dict = dict(izip(col_names, row))
           value.append(row_dict)
       yield value
   except:
       value = [{'status':0, 'message':'Error SQL Process'}]
       yield value
       return
   finally:
       #cursor.close()
       return


