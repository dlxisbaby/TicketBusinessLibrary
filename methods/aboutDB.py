#coding:utf-8

try:
    import pymysql
    import config
except ImportError:
    from TicketBusinessLibrary.libs import pymysql
    from TicketBusinessLibrary import config

import sys
reload(sys)
sys.setdefaultencoding("utf8")

from robot.api import logger

class Database():
    def __init__(self,ip='',port='',user='',passwd=''):
        self.ip = ip
        self.port = int(port)
        self.user = user
        self.passwd = passwd

    def DB_select_by_sql(self,db_name,sql):
        conn = pymysql.connect(host=self.ip,port=3306,user=self.user,passwd=self.passwd,db=db_name,charset="utf8")
        cur = conn.cursor()
        cur.execute(sql)
        fetchall = cur.fetchall()
        return fetchall

    def DB142_Select(self,table,key="*",condition=''):
        datas = DB(config.cinema_info["mysql_db"],table)._select(key)._where(condition)._submit(config.cinema_info["ip"],3306,config.cinema_info["mysql_user"],config.cinema_info["mysql_passwd"])
        return datas

    def DBMid_Select(self,table,key="*",condition=''):
        datas = DB(config.mid_info["mysql_db"],table)._select(key)._where(condition)._submit(config.mid_info["ip"],3306,config.mid_info["mysql_user"],config.mid_info["mysql_passwd"])
        return datas


class DB():
    def __init__(self,db,table):
        self.db = db
        self.table = table

    def _select(self,keys="*"):
        '''
        输入查询字段
        :param keys: 查询的字段
        :return:
        '''
        sql = "select {0} from {1}".format(keys,self.table)
        return Condition(self.db,sql)

class Condition():
    def __init__(self,db,sql):
        self.db = db
        self.sql = sql

    def _where(self,kwargs=''):
        '''
        输入匹配的where条件，跟随在select后
        :param kwargs: where条件，字典类型
        :return:
        '''
        if kwargs:
            condition = " where 1=1 AND "
        else:
            condition = " where 1=1 "

        _filter = " AND ".join(["{0}='{1}'".format( k, kwargs.get(k)) for k in kwargs])
        sql = self.sql+condition+_filter
        return Handle(self.db,sql)

class Handle():
    def __init__(self,db,sql):
        self.db = db
        self.sql = sql

    def _submit(self,url,port,user,passwd):
        '''
        提交查询，跟随在where后
        :return:
        '''
        logger.info(u"执行的sql为：{0}".format(self.sql))
        conn = pymysql.connect(host=url,port=port,user=user,passwd=passwd,db=self.db,charset="utf8")
        cur = conn.cursor()
        cur.execute(self.sql)
        fetchall = cur.fetchall()
        return fetchall

if __name__ == "__main__":
    a = Database("192.168.3.142","3306","root","123456").DB_select_by_sql("tms","select name from tms_retail_goods")
    print a
    #b = DB("tms","tms_retail_goods")._select()._where({"id":1})._submit("192.168.3.142",3306,"root","123456")
    #print b[0]

