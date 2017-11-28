#coding:utf-8

from collections import OrderedDict

class Dict():
    def __init__(self):
        pass

    def dlx_make_list_to_ordered_dict_list(self,normal_dict,level_num):
        '''
        level_num为父层级的数量
        normal_dict为需要转化为有序字典的字典，格式为：\
        {"level_name":"Film"\
        "level_tag_name_list":["FilmNo","FilmName","FilmType","Language"],\
        "level_tag_value_list":[FilmNo_list,FilmName_list,FilmType_list,Language_list],\
        "group_list":["3","1","3"]}
        level_name_list为层级名称列表，tag_name_list为标签内容列表，\
        tag_value_list为每个标签内容列表的集合,列表中的内容必须为同一类型\n
        '''
        order_dict1 = OrderedDict()
        length2 = len(normal_dict["level_tag_name_list"])
        list_final = []
        if normal_dict.has_key("group_list") == True:
            length1 = len(normal_dict["level_tag_value_list"][0])
            ordered_dict_list = []
            num = 0
            dict2 = {}
            for i in range(0,length1):
                k = 0
                while k < length2:
                    order_dict1[str(normal_dict["level_tag_name_list"][k]).decode("utf-8")] = str(normal_dict["level_tag_value_list"][k][i]).decode("utf-8")
                    k = k + 1
                dict2 = order_dict1.copy()
                ordered_dict_list.append(dict2)
            num_temp = 0
            for i in normal_dict["group_list"]:
                ordered_dict = OrderedDict()
                list_temp = ordered_dict_list[num_temp:num_temp+int(i)]
                num_temp = num_temp+int(i)
                if int(i) == 1:
                    ordered_dict[normal_dict["level_name"]] = list_temp[0]
                    list_final.append(ordered_dict)
                else:
                    ordered_dict[normal_dict["level_name"]] = list_temp
                    list_final.append(ordered_dict)
            return list_final
        else:
            ordered_dict_list = []
            if type(normal_dict["level_tag_value_list"][0]) == list:
                length1 = len(normal_dict["level_tag_value_list"][0])
                for i in range(0,length1):
                    k = 0
                    while k < length2:
                        order_dict1[str(normal_dict["level_tag_name_list"][k]).decode("utf-8")] = str(normal_dict["level_tag_value_list"][k][i]).decode("utf-8")
                        k = k + 1
                    dict2 = order_dict1.copy()
                    ordered_dict_list.append(dict2)
                    if normal_dict["level_name"] == '':
                        if int(level_num) == 1:
                            #ordered_dict = ordered_dict_list[0]
                            ordered_dict = ordered_dict_list
                        else:
                            ordered_dict = ordered_dict_list[i]
                            #ordered_dict = ordered_dict_list[i][0]
                    else:
                        ordered_dict = OrderedDict()
                        if int(level_num) == 1:
                            ordered_dict[normal_dict["level_name"]] = ordered_dict_list
                            #ordered_dict[normal_dict["level_name"]] = ordered_dict_list[0]
                        else:
                            ordered_dict[normal_dict["level_name"]] = ordered_dict_list[i]
                            #ordered_dict[normal_dict["level_name"]] = ordered_dict_list[i][0]
                    list_final.append(ordered_dict)
                return list_final
            else:
                k = 0
                while k < length2:
                    order_dict1[str(normal_dict["level_tag_name_list"][k]).decode("utf-8")] = str(normal_dict["level_tag_value_list"][k]).decode("utf-8")
                    k = k + 1
                dict2 = order_dict1.copy()
                ordered_dict = OrderedDict()
                ordered_dict[normal_dict["level_name"]] = dict2
                list_final.append(ordered_dict)
                return list_final

    def _make_list_to_ordereddict_list(self,up_level,level_name_list,*level_value_list):
        '''
        生成一个有序字典列表
        :param up_level: 上级名称
        :param level_name_list: 层级名称列表level_name_list=[u'FilmNo', u'FilmName', u'FilmType', u'Language']
        :param level_value_list: 层级值列表，需要与层级名称列表中的值一一对应FilmNo_list,FilmName_list,FilmType_list,Language_list
        '''
        if len(level_name_list) != len(level_value_list):
            raise ValueError(u"名称列表与值列表长度不一致")
        final_list = []
        dict1 = OrderedDict()
        for i in range(len(level_name_list)):
            for j in range(len(level_name_list)):
                if type(level_value_list[j][i]) == unicode:
                    dict1[level_name_list[j]] = level_value_list[j][i]
                else:
                    dict1[level_name_list[j]] = str(level_value_list[j][i]).decode("utf-8")
            temp = dict1.copy()
            final_list.append(temp)
        dict2 = OrderedDict()
        final_list2 = []
        for i in final_list:
            dict2[up_level] = i
            temp = dict2.copy()
            final_list2.append(temp)
        return final_list2

if __name__ == "__main__":
    aa = {u'Films': OrderedDict([(u'Film', OrderedDict([(u'FilmNo', u'458'), (u'FilmName', u'\u72c2\u517d(2D)'), (u'FilmType', u'2d'), (u'Language', u'cn')]))])}
    FilmNo_list = [458, 438, 183, 439]
    FilmName_list = [u'\u72c2\u517d(2D)', u'\u5206\u7c7b\u7ec6\u5316(\u4e2d\u56fd\u5de8\u5e553D22)', u'\u6e44\u516c\u6cb3\u884c\u52a8(\u4e2d\u56fd\u5de8\u5e55)', u'\u4e5d\u4e00\u516b(\u5f71\u5c55\u89c2\u6469\u7247)']
    FilmType_list = [u'2d', u'dmax3d', u'3d', u'view']
    Language_list = [u'cn', u'cn', u'cn', u'cn']

    level_name_list = [u'FilmNo', u'FilmName', u'FilmType', u'Language']

    cc = Dict()._make_list_to_ordereddict_list("Film",level_name_list,FilmNo_list,FilmName_list,FilmType_list,Language_list)
    print cc
    #print cc[0]
    #print aa["Films"]["Film"]
