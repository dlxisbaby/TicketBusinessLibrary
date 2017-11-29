#coding:utf-8

import sys,hashlib
reload(sys)
sys.setdefaultencoding('utf8')


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
                #i = String()._make_all_element_to_unicode(i)
                obj[i] = String()._make_all_element_to_unicode(obj[i])
        elif type(obj) != unicode:
                obj = str(obj).decode("utf-8")
        return obj

if __name__ == "__main__":
    a = [1,2,3]
    c = {"a":1,"v":2}
    b = String()._make_all_element_to_unicode(c)
    print b

