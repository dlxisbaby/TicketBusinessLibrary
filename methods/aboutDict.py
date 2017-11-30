#coding:utf-8

from collections import OrderedDict

class Dict():
    def __init__(self):
        pass

    def _orderdict_to_dict(self,obj):
        '''
        使用递归法，将目标对象中的有序字段转化为普通字典
        :param obj:被转化的对象
        '''
        if type(obj) == list or type(obj) == tuple:
            for i in obj:
                Dict()._orderdict_to_dict(i)
        elif type(obj) == dict:
            for i in obj:
                obj[i] = Dict()._orderdict_to_dict(obj[i])
        elif type(obj) == OrderedDict:
            obj = dict(obj)
            Dict()._orderdict_to_dict(obj)
        return obj

    def _make_list_to_dict_list(self,up_level,level_name_list,*level_value_list):
        '''
        生成一个字典列表
        :param up_level: 比level_name更上一级的名称
        :param level_name_list: 层级名称列表level_name_list=[u'FilmNo', u'FilmName', u'FilmType', u'Language']
        :param level_value_list: 层级值列表，需要与层级名称列表中的值一一对应FilmNo_list,FilmName_list,FilmType_list,Language_list
        '''
        if len(level_name_list) != len(level_value_list):
            raise ValueError(u"名称列表与值列表长度不一致")
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
        for i in final_list:
            dict2[up_level] = i
            temp = dict2.copy()
            final_list2.append(temp)
        return final_list2

if __name__ == "__main__":
    aa = {u'Films': OrderedDict([(u'Film', OrderedDict([(u'FilmNo', u'458'), (u'FilmName', u'\u72c2\u517d(2D)'), (u'FilmType', u'2d'), (u'Language', u'cn')]))])}
    FilmNo_list = [183, 439, 458, 438, 183, 439]
    FilmName_list = [u'\u6e44\u516c\u6cb3\u884c\u52a8(\u4e2d\u56fd\u5de8\u5e55)', u'\u4e5d\u4e00\u516b(\u5f71\u5c55\u89c2\u6469\u7247)', u'\u72c2\u517d(2D)', u'\u5206\u7c7b\u7ec6\u5316(\u4e2d\u56fd\u5de8\u5e553D22)',u'\u6e44\u516c\u6cb3\u884c\u52a8(\u4e2d\u56fd\u5de8\u5e55)', u'\u4e5d\u4e00\u516b(\u5f71\u5c55\u89c2\u6469\u7247)']
    FilmType_list = [u'3d', u'view', u'2d', u'dmax3d', u'3d', u'view']
    Language_list = [u'cn', u'cn', u'cn', u'cn', u'cn', u'cn']

    level_name_list = [u'FilmNo', u'FilmName', u'FilmType', u'Language']

    cc = Dict()._make_list_to_dict_list("Film",level_name_list,FilmNo_list,FilmName_list,FilmType_list,Language_list)
    print cc
    print len(cc)
    #print cc[0]
    #print aa["Films"]["Film"]
