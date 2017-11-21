#coding:utf-8

from decimal import Decimal
from aboutString import String

class List():
    def __init__(self):
        pass

    def _db_list_to_standard_list(self,db_list,mode="1"):
        '''
        将查询数据库的列表，如：
        [(1,), (3,), (15,), (16,), (17,), (18,), (19,), (20,)]
        转化为标准列表
        [1, 3, 15, 16, 17, 18, 19, 20](mode=1时)
        [u'1',u'3',u'15',u'17',u'18',u'19',u'20'](mode=2时)
        '''
        final_list = []
        for i in db_list:
            if mode == "1":
                if type(i[0]) == int or type(i[0]) == Decimal():
                    final_list.append(i[0])
                elif type(i[0]) == unicode():
                    for ch in i[0]:
                        if String._check_str_contain_chinese(ch):
                            final_list.append(i[0])
                            break
                        else:
                            final_list.append(i[0].encode("utf-8"))
                            break
                else:
                    final_list.append(i[0].encode("utf8"))
            elif mode == "2":
                final_list.append(str(i[0]).decode("utf8"))
        return final_list

if __name__ == "__main__":
    a = [(u"是",), (u"是",), (u"是",), (u"是",), (u"是",), (u"是",)]
    b = List()._db_list_to_standard_list(a,"2")
    print b


