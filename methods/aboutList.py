#coding:utf-8

from decimal import Decimal
from aboutString import String
from robot.api import logger
import operator
import json

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


    def _sql_list_to_dict_list(self,tag_name_list,*tag_value_lists):
        '''
        tag_value_lists = [list1,list2,list3,……]\n
        tag_value_lists的长度应等于tag_name_list的长度\n
        将tag_value_lists中每个列表的第一个值赋值给tag_name_list列表，\
        形成字典，以此类推，最后生成值为字典的列表\n
        '''
        if len(tag_name_list) != len(tag_value_lists):
            raise ValueError(u"tag_name_list长度与tag_value_lists长度不相等")
        else:
            length = len(tag_value_lists[0])
            for i in tag_value_lists:
                if len(i) != length:
                    raise ValueError(u"tag_value_lists中的列表长度不相等")
        final_dict = {}
        final_list = []
        length = len(tag_name_list)
        for i in range(len(tag_value_lists[0])):
            k = 0
            while k < length:
                final_dict[tag_name_list[k]] = str(tag_value_lists[k][i]).decode("utf-8")
                k += 1
            dict2 = final_dict.copy()
            final_list.append(dict2)
        return final_list

    def _sql_single_to_dict(self,tag_name_list,*tag_value):
        '''
        tag_value为各个变量\n
        tag_value的长度应等于tag_name_list的长度\n
        将tag_value中每个值赋值给tag_name_list列表，\
        最后生成为字典\n
        '''
        if len(tag_name_list) != len(tag_value):
            raise u"tag_name_list长度与tag_value_lists长度不相等"
        final_dict = {}
        length = len(tag_name_list)
        for i in range(length):
            final_dict[tag_name_list[i]] = str(tag_value[i]).decode("utf-8")
        return [final_dict]

    def _remove_float_end_zero(self,list_begin):
        '''
        消除列表里面float类型尾部的0
        '''
        list_after = []
        for i in list_begin:
            i = float(i)
            num_str = str(i)
            if num_str[-1] == '0':
                list_after.append(int(i))
            else:
                list_after.append(i)
        return list_after

    def _contact_two_dict_list(self,list_main,list_order,key_name):
        '''
        连接2个字典列表，key_name是list_main中的字典需要新加的key
        '''
        if len(list_main) != len(list_order):
            raise ValueError(u"两个列表长度不相等")
        length1 = len(list_main)
        new_key = str(key_name).decode("utf-8")
        if length1 == 1:
            list_main[0][new_key] = list_order[0]
            return list_main
        else:
            for i in range(length1):
                list_main[i][new_key] = list_order[i]
            return list_main

    def _get_n_length_same_value_list(self,n,value,mode=1):
        '''
        N为3，value为None\n
        mode为1生成[u'None',u'None',u'None']\n
        mode为2生成['None','None','None']\n
        mode为3生成[None,None,None]\n
        :param n: 列表长度\n
        :param value: 列表的值\n
        '''
        final_list = []
        for i in range(int(n)):
            if int(mode) == 1:
                final_list.append(str(value).decode("utf-8"))
            elif int(mode) == 2:
                final_list.append(str(value).encode("utf-8"))
            elif int(mode) == 3:
                final_list.append(value)
        return final_list

    def _sort_dictlist(self,dict_list,order_by):
        '''
        对一个字典列表进行排序
        :param dict_list: 排序的字典列表
        :param order_by: 排序的键
        :return:
        '''

        if order_by == '':
            return dict_list
        final_list = []
        try:
            for i in dict_list:
                i = json.loads(i)
                i[order_by] = int(i[order_by])
                final_list.append(i)
            final_list.sort(key=operator.itemgetter(order_by))
            for i in final_list:
                i[order_by] = str(i[order_by]).decode("utf-8")
            return final_list
        except ValueError:
            raise ValueError(u"排序的key不是数字")




if __name__ == "__main__":

    b = List()._sort_dictlist(a1,"seat_id")
    print b
