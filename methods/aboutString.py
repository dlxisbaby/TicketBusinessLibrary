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



if __name__ == "__main__":
    a = "aaa"
    b = String()._check_str_contain_chinese(a)
    print b
