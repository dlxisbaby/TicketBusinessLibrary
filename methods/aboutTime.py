#coding:utf-8

import time,datetime


class Time():
    def __init__(self):
        pass

    def _get_current_unix_time(self):
        '''
        获得当前时间的unix时间戳字符串
        '''
        format1 = '%Y-%m-%d %H:%M:%S'
        time1 = time.localtime()
        s = time.mktime(time1)
        return str(int(s))

    def _get_current_date_and_time(self):
        '''
        获得当前日期和时间的字符串
        '''
        format1 = '%Y-%m-%d %H:%M:%S'
        time1 = time.localtime()
        value = time.strftime(format1,time1)
        return str(value)

    def _get_current_date(self,separate="-"):
        '''
        获得当前日期的字符串
        '''
        format1 = '%Y{0}%m{0}%d'.format(separate)
        time1 = time.localtime()
        value = time.strftime(format1,time1)
        return str(value)

    def _get_current_time(self,separate=":"):
        '''
        获得当前日期的字符串
        '''
        format1 = '%H{0}%M{0}%S'.format(separate)
        time1 = time.localtime()
        value = time.strftime(format1,time1)
        return str(value)

    def _get_date(self,way='',num=''):
        '''
        获取日期，way是after时获取当前日期之后的num天的日期
        way:是after或者before
        num:平移的天数
        '''
        if way == "after":
            date = datetime.date.today() + datetime.timedelta(int(num))
        elif way == "before":
            date = datetime.date.today() - datetime.timedelta(int(num))
        else:
            date = datetime.date.today()
        return date

if __name__ == "__main__":
    a = Time()._get_date("before","2")
    print a
