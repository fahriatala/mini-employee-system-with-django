from employee.define import m_database

class AuthRouter(object):
    """
    A router to control all database operations on models in the
    application.
    """

    
    def allow_relation(self, obj1, obj2, **hints):
       return True

    def allow_migrate(self, db, model):
        return allow_dba(model._meta.db_table)



def allow_dba(table):
  #AUTH_DB -> ISI LIST TABEL ->MODEL
    m_databases = dict()
    m_databases = m_database

    for k, v in m_databases.items():
      if table in v:
        return str(k)
        break

    return 'data'