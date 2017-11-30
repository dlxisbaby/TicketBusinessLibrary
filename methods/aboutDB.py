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
    def __init__(self,cinema_code='',session_code=''):
        self.cinema_code = cinema_code
        self.session_code = session_code

    def _get_seat_info_from_redis(self,seat_status="",order_by="seat_id"):
        '''
        从redis中获取座位数据
        seat_status为座位状态，可售available，不可售unavailable，\n
        已锁定locked，已售sold
        '''
        if self.cinema_code == '' or self.session_code == '':
            raise ValueError(u"cinema_code和session_code为必填项")
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

    def _get_status_list_from_redis(self,seat_info_list):
        '''
        返回座位状态的列表
        seat_info_list:座位信息字典列表
        '''
        final_list = []
        for i in seat_info_list:
            if i['status'] == "available":
                final_list.append(0)
            elif i['status'] == "sold":
                final_list.append(1)
            elif i['status'] == "locked":
                final_list.append(3)
            else:
                 final_list.append(-1)
        return final_list

    def _get_seat_info_from_dictlist(self,dictlist,seat_id,key=''):
        '''
        获取指定座位id的key的值
        :param dictlist:所有座位信息的字典列表
        :param seat_id:座位id
        :param key:需要获取的key
        '''
        seat_id = str(seat_id)
        for i in dictlist:
            if key == "":
                if i["seat_id"] == seat_id:
                    return i
            elif key not in i.keys():
                raise ValueError(u"key输入错误，不存在这个key")
            else:
                if i["seat_id"] == seat_id:
                    logger.info(i[key])
                    return i[key]

    def _get_available_seatid_from_dictlist(self,dictlist,num="1"):
        '''
        获取可用座位的ID
        :param dictlist: 所有座位信息的字典列表
        num为返回的ID数量，默认为1
        '''
        if num == "1":
            for i in dictlist:
                if i["status"] == "available":
                    return i["seat_id"]
        else:
            try:
                num = int(num)
                final_string = ""
                for i in dictlist:
                    if i["status"] == "available":
                        final_string = final_string + str(i["seat_id"]) + ","
                    if len(final_string.split(",")) == num+1:
                        break
                return final_string[:-1]
            except ValueError:
                raise ValueError(u"num参数必须是整数")

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
    a = Redis("10000142","42f5db4a353c746b")._get_seat_info_from_redis()
    #print a
    b = Redis()._get_available_seatid_from_dictlist(a,"3")
    print b
    #aa = ''
    #bb = aa.join("444")
    #cc = bb.join("222")
    #print cc
