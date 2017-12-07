#coding:utf-8
from decimal import Decimal

class Number():
    def __init__(self):
        pass

    def _remove_zero(self,obj):
        '''
        移除对象中无用的0后返回同样的数据类型
        :param obj: 被移除对象（可以是变量、列表、字典、元组）
        '''
        if type(obj) == list or type(obj) == tuple:
            for i in range(len(obj)):
                obj[i] = self._remove_zero(obj[i])
        elif type(obj) == dict:
            for i in obj:
                obj[i] = self._remove_zero(obj[i])
        else:
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

    def _num_to_decimal(self,num,num_format="0.00"):
        '''
        将目标中的数字转化为指定格式
        :param num: 目标（单个数字、列表、元组、字典等）
        :param num_format: 指定的格式，默认为0.00
        '''
        if type(num) == list or type(num) == tuple:
            for i in range(len(num)):
                num[i] = self._num_to_decimal(num[i],num_format)
                #i = self._num_to_decimal(i,num_format)
                #print num[i]
        elif type(num) == dict:
            for i in num:
                num[i] = self._num_to_decimal(num[i],num_format)
        else:
            try:
                num = Decimal(num).quantize(Decimal(num_format))
            except:
                raise ValueError(u"不是数字不能转换")
        return num

if __name__ == "__main__":
    aa = 1/3.0
    a = Number()._num_to_decimal(aa)
    print aa
