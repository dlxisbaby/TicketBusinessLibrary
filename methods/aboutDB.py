#coding:utf-8

try:
    import pymysql
    import config
    import redis
except ImportError:
    from TicketBusinessLibrary.libs import pymysql
    from TicketBusinessLibrary.libs import redis
    from TicketBusinessLibrary import config

import sys,operator
reload(sys)
sys.setdefaultencoding("utf8")

from robot.api import logger
from TicketBusinessLibrary.methods.aboutList import List

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

class Redis():
    def __init__(self,cinema_code,session_code):
        self.cinema_code = cinema_code
        self.session_code = session_code

    def _get_seat_info_from_redis(self,order_by="seat_id"):
        r = redis.Redis(host="172.16.200.233",port="6379",db=0)
        string1 = r.hgetall("CACHE:HASH:SESSIONSEAT:{0}:{1}".format(self.cinema_code,self.session_code))
        dict_list = string1.values()
        #final_list = List()._sort_dictlist(dict_list,order_by)
        return dict_list

    def _get_value_list_from_redis22(self,cinema_code,session_code,order_by_key):
        '''
        从redis中获取座位数据
        '''
        r = redis.Redis(host="172.16.200.233",port="6379",db=0)
        string1 = r.hgetall("CACHE:HASH:SESSIONSEAT:{0}:{1}".format(cinema_code,session_code))
        list1 = string1.values()
        print list1
        list_final = []
        list_sorted = []
        for i in list1:
            dict1 = eval(i)
            if type(dict1[order_by_key]) != int:
                dict1[order_by_key] = int(dict1[order_by_key])
                list_sorted.append(dict1)
        list_sorted.sort(key=operator.itemgetter(order_by_key))
        for i in list_sorted:
            i[order_by_key] = str(i[order_by_key])
            if i["status"] == "available":
                list_final.append("0")
            elif i["status"] == "sold":
                list_final.append("1")
            elif i["status"] == "locked":
                list_final.append("3")
            else:
                list_final.append("-1")
        return list_final

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
            kwargs = dict(kwargs)
            logger.info(kwargs)
            condition = " where 1=1 AND "
        else:
            condition = " where 1=1 "

        _filter = " AND ".join(["{0}='{1}'".format( k, kwargs.get(k)) for k in kwargs])
        logger.info(u"condition为：{0}".format(_filter))
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
    a = Redis("10000142","15bb78b0d1d24bbb")._get_seat_info_from_redis()
    print a
    print len(a)
    b = List()._sort_dictlist(a,"seat_id")
    #print b

