#coding:utf-8

import sys,hashlib
reload(sys)
sys.setdefaultencoding('utf8')
from random import Random


class String():
    def __init__(self):
        pass

    def _check_str_contain_chinese(self,string):
        '''
        检查字符串是否包含中文
        :param check_str:被检查得字符串
        '''
        for ch in string.decode('utf-8'):
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    def _md5_32_lowercase(self,string):
        '''
        对字符串进行32位小写的MD5加密
        '''
        m = hashlib.md5()
        m.update(string)
        encrypted_string = m.hexdigest()
        return encrypted_string

    def _make_string_for_sql(self,list_obj):
        '''
        转换一个列表给数据库的in关键字使用
        '''
        final_string = ''
        for i in list_obj:
            i = "\"{0}\"".format(i)
            final_string = final_string + i + ","
        return final_string[:-1]

    def _make_all_element_to_unicode(self,obj):
        if type(obj) == list or type(obj) == tuple:
            for i in range(len(obj)):
                obj[i] = String()._make_all_element_to_unicode(obj[i])
        elif type(obj) == dict:
            for i in obj:
                temp_key = String()._make_all_element_to_unicode(i)
                temp_value = String()._make_all_element_to_unicode(obj[i])
                obj.pop(i)
                obj[temp_key] = temp_value
        elif type(obj) != unicode:
                obj = str(obj).decode("utf-8")
        return obj

    def _get_n_length_random_num(self,n,mode="1"):
        '''
        获取一个N位长度的随机数，mode为1时返回字符串格式\n
        mode为2时返回整型格式
        :param n: 返回的长度
        '''
        n = int(n)
        min = 10**(n-1)
        max = 10**n-1
        num = Random().randint(min,max)
        if mode == "1":
            return str(num)
        elif mode == "2":
            return num

if __name__ == "__main__":
    a = [1,2,3]
    c = [{"a":"a","v":2},3,3]
    b = String()._get_n_length_random_num(12)
    #print b

