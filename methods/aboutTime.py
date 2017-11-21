#coding:utf-8

import time


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

if __name__ == "__main__":
    a = Time()._get_current_time()
    print a
