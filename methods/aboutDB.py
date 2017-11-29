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

    def _get_seat_info_from_redis(self,seat_status="",order_by="seat_id"):
        '''
        从redis中获取座位数据
        seat_status为座位状态，可售available，不可售unavailable，\n
        已锁定locked，已售sold
        '''
        r = redis.Redis(host=config.mid_info["ip"],port="6379",db=0)
        string1 = r.hgetall("CACHE:HASH:SESSIONSEAT:{0}:{1}".format(self.cinema_code,self.session_code))
        dict_list = string1.values()
        final_list = List()._sort_dictlist(dict_list,order_by)
        #返回所传状态的座位
        if seat_status == "":
            return final_list
        else:
            seat_list = []
            for i in range(len(final_list)):
                if final_list[i]['status'] == seat_status:
                    seat_list.append(final_list[i])
                else:
                    continue
            return seat_list


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
    #b = List()._sort_dictlist(a,"seat_id")
    #print b

