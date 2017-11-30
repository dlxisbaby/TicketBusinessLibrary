#coding:utf-8

class Number():
    def __init__(self):
        pass

    def _remove_zero_from_float(self,obj):
        obj = str(obj)
        length = len(obj)
        for i in range(1,length+1):
            if obj[-1] == "0":
                obj = obj[:-1]
            else:
                break
        if obj[-1] == ".":
            obj = obj[:-1]
        else:
            obj = float(obj)
        return obj

    def _remove_zero_from_list_or_tuple(self,obj):
        list_leng = len(obj)
        for i in range(0,list_leng):
            if type(obj[i]) == int:
                continue
            else:
                temp = str(obj[i])
                length = len(temp)
                for j in range(1,length+1):
                    if temp[-1] == "0":
                        temp = temp[:-1]
                    else:
                        break
                if temp[-1] == ".":
                    temp = int(temp[:-1])
                else:
                    temp = float(temp)
                obj[i] = temp
        return obj

    def _convert_dict_list_to_float(self,dict_list,fields):
        '''
        将dict_list中的字典的字段值转化为float类型
        '''
        for i in dict_list:
            for j in i:
                if type(fields) == list:
                    if j in fields:
                        i[j] = str(float(i[j])).decode("utf-8")
                else:
                    if j == fields:
                        i[j] = str(float(i[j])).decode("utf-8")
        return dict_list

    def _sure_data_not_null(self,obj):
        if len(obj) == 0:
            raise ValueError(u"此数据为空")
        else:
            return obj
