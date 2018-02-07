#coding:utf-8

from collections import OrderedDict
from TicketBusinessLibrary.methods.aboutList import List

class Dict():
    def __init__(self):
        pass

    def _orderdict_to_dict(self,obj):
        '''
        使用递归法，将目标对象中的有序字段转化为普通字典
        :param obj:被转化的对象
        '''
        if type(obj) == list or type(obj) == tuple:
            for i in range(len(obj)):
                if type(obj[i]) == OrderedDict:
                    obj[i] = dict(obj[i])
                    self._orderdict_to_dict(obj[i])
                else:
                    self._orderdict_to_dict(obj[i])
        elif type(obj) == dict:
            for i in obj:
                #print "{0}:{1}".format(i,obj[i])
                if type(obj[i]) == OrderedDict:
                    #print "{0}:{1}".format(i,obj[i])
                    obj[i] = dict(obj[i])
                    self._orderdict_to_dict(obj[i])
                else:
                    self._orderdict_to_dict(obj[i])
        return obj

    def _make_list_to_dict_list(self,up_level,level_name_list,*level_value_list):
        '''
        生成一个字典列表
        :param up_level: 比level_name更上一级的名称
        :param level_name_list: 层级名称列表level_name_list=[u'FilmNo', u'FilmName', u'FilmType', u'Language']
        :param level_value_list: 层级值列表，需要与层级名称列表中的值一一对应FilmNo_list,FilmName_list,FilmType_list,Language_list
        '''
        if len(level_name_list) != len(level_value_list):
            raise ValueError(u"名称列表与值列表长度不一致\n名称列表长度为:{0}\n值列表长度为:{1}".format(len(level_name_list),len(level_value_list)))
        final_list = []
        dict1 = {}
        if type(level_value_list[0]) == list or type(level_value_list[0]) == tuple:
            for i in range(len(level_value_list[0])):
                for j in range(len(level_name_list)):
                    if type(level_value_list[j][i]) == unicode:
                        dict1[level_name_list[j]] = level_value_list[j][i]
                    else:
                        dict1[level_name_list[j]] = str(level_value_list[j][i]).decode("utf-8")
                temp = dict1.copy()
                final_list.append(temp)
        else:
            for i in range(len(level_name_list)):
                if type(level_value_list[i]) == unicode:
                    dict1[level_name_list[i]] = level_value_list[i]
                else:
                    dict1[level_name_list[i]] = str(level_value_list[i]).decode("utf-8")
            final_list.append(dict1)
        dict2 = {}
        final_list2 = []
        if up_level == "":
            return final_list
        else:
            for i in final_list:
                dict2[up_level] = i
                temp = dict2.copy()
                final_list2.append(temp)
            return final_list2

    def _make_list_to_dict_list_with_group(self,up_level,group_list,level_name_list,*level_value_list):
        '''
        生成一个字典列表
        up_level: 比level_name更上一级的名称
        level_name_list: 层级名称列表level_name_list=[u'FilmNo', u'FilmName', u'FilmType', u'Language']
        group_list:分组的数量列表
        level_value_list: 层级值列表，需要与层级名称列表中的值一一对应FilmNo_list,FilmName_list,FilmType_list,Language_list
        '''
        if len(level_name_list) != len(level_value_list):
            raise ValueError(u"名称列表与值列表长度不一致\n名称列表长度为:{0}\n值列表长度为:{1}".format(len(level_name_list),len(level_value_list)))
        final_list = []
        dict1 = {}
        if type(level_value_list[0]) == list or type(level_value_list[0]) == tuple:
            for i in range(len(level_value_list[0])):
                for j in range(len(level_name_list)):
                    if type(level_value_list[j][i]) == unicode:
                        dict1[level_name_list[j]] = level_value_list[j][i]
                    else:
                        dict1[level_name_list[j]] = str(level_value_list[j][i]).decode("utf-8")
                temp = dict1.copy()
                final_list.append(temp)
        else:
            for i in range(len(level_name_list)):
                if type(level_value_list[i]) == unicode:
                    dict1[level_name_list[i]] = level_value_list[i]
                else:
                    dict1[level_name_list[i]] = str(level_value_list[i]).decode("utf-8")
            final_list.append(dict1)
        print final_list
        dict2 = {}
        final_list3 = []
        num = 0
        for k in group_list:
            temp_list = []
            for i in range(len(final_list)):
                if i != int(k) and k != 1:
                    temp_list.append(final_list[num])
                    num += 1
                elif i != int(k) and k == 1:
                    dict2[up_level] = final_list[num]
                    final_list3.append(dict2.copy())
                    num += 1
                    break
                else:
                    dict2[up_level] = temp_list
                    final_list3.append(dict2.copy())
                    break
        return final_list3

if __name__ == "__main__":

    group_list = [3, 1, 3]
    up_level = "seat_info"
    level_name_list = ["SeatNo"]
    seat_no_list = [15912, 15913, 15914, 15911, 27529, 27530, 27531]
    #seat_no_list2 = [15912, 15913, 15914, 15911, 27529, 27530, 27531]

    a = Dict()._make_list_to_dict_list(up_level,level_name_list,seat_no_list)
    print a
    #print len(a)

