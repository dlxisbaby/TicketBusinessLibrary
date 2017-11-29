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
    a1 = ['{"id":0,"seat_code":"730a35762446e246","seat_id":"4639","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"4","column_num":"2","status":"available","update_time":0,"x_coord":"2","y_coord":"4","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"ca814d565d535848","seat_id":"4654","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"5","column_num":"7","status":"available","update_time":0,"x_coord":"7","y_coord":"5","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"9398c9f24f30ce11","seat_id":"4672","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"7","column_num":"5","status":"available","update_time":0,"x_coord":"5","y_coord":"7","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"fddd1d38c6adcf91","seat_id":"4642","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"4","column_num":"5","status":"available","update_time":0,"x_coord":"5","y_coord":"4","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"c2c143c47e8f9a58","seat_id":"4707","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"10","column_num":"10","status":"available","update_time":0,"x_coord":"10","y_coord":"10","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"5d8bfce79dc2e660","seat_id":"4667","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"6","column_num":"10","status":"available","update_time":0,"x_coord":"10","y_coord":"6","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"e9e652f8a6bfaed6","seat_id":"4698","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"10","column_num":"1","status":"available","update_time":0,"x_coord":"1","y_coord":"10","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"34ef9ced0fcaf9ab","seat_id":"4679","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"8","column_num":"2","status":"available","update_time":0,"x_coord":"2","y_coord":"8","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"8240600a65483d22","seat_id":"4692","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"9","column_num":"5","status":"available","update_time":0,"x_coord":"5","y_coord":"9","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"af2bab073c318a7a","seat_id":"4624","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"2","column_num":"4","status":"available","update_time":0,"x_coord":"6","y_coord":"2","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"0826b186698d6f22","seat_id":"4702","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"10","column_num":"5","status":"available","update_time":0,"x_coord":"5","y_coord":"10","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"90f9655f78d8385e","seat_id":"4684","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"8","column_num":"7","status":"available","update_time":0,"x_coord":"7","y_coord":"8","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"9395ad45a34ce216","seat_id":"4613","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"4","row_num":"1","column_num":"3","status":"available","update_time":0,"x_coord":"4","y_coord":"1","bind_id":"0","seat_type_id":"3","seat_type_desc":"VIP\\u5ea7"}', '{"id":0,"seat_code":"4505ac822c761223","seat_id":"4640","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"4","column_num":"3","status":"available","update_time":0,"x_coord":"3","y_coord":"4","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"833c841100efd42b","seat_id":"4676","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"7","column_num":"9","status":"available","update_time":0,"x_coord":"9","y_coord":"7","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"1929646b5f727ac7","seat_id":"4686","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"8","column_num":"9","status":"available","update_time":0,"x_coord":"9","y_coord":"8","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"0685fbac4590fabf","seat_id":"4696","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"9","column_num":"9","status":"available","update_time":0,"x_coord":"9","y_coord":"9","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"4925e60d9e58b771","seat_id":"4622","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"2","column_num":"2","status":"available","update_time":0,"x_coord":"4","y_coord":"2","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"6db99de34c2bb9ac","seat_id":"4645","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"4","column_num":"8","status":"available","update_time":0,"x_coord":"8","y_coord":"4","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"49c83a05cbc982e8","seat_id":"4688","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"9","column_num":"1","status":"available","update_time":0,"x_coord":"1","y_coord":"9","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"e6e3579a91dbe189","seat_id":"4671","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"7","column_num":"4","status":"available","update_time":0,"x_coord":"4","y_coord":"7","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"dba3c17b2a77bf30","seat_id":"4618","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"1","column_num":"8","status":"available","update_time":0,"x_coord":"9","y_coord":"1","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"5b5988a363567698","seat_id":"4675","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"7","column_num":"8","status":"available","update_time":0,"x_coord":"8","y_coord":"7","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"838a03811791ab51","seat_id":"4626","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"2","column_num":"6","status":"available","update_time":0,"x_coord":"8","y_coord":"2","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"ad5551ef0dd979a1","seat_id":"4660","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"6","column_num":"3","status":"available","update_time":0,"x_coord":"3","y_coord":"6","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"df42e3f1f5140930","seat_id":"4666","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"6","column_num":"9","status":"available","update_time":0,"x_coord":"9","y_coord":"6","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"1027b67d02b41551","seat_id":"4673","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"7","column_num":"6","status":"available","update_time":0,"x_coord":"6","y_coord":"7","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"5abd1a583d67ec1a","seat_id":"4631","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"3","column_num":"4","status":"available","update_time":0,"x_coord":"4","y_coord":"3","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"3acd54363ce28e83","seat_id":"4616","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"1","column_num":"6","status":"unavailable","update_time":0,"x_coord":"7","y_coord":"1","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"6533d984665fe30c","seat_id":"4704","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"10","column_num":"7","status":"available","update_time":0,"x_coord":"7","y_coord":"10","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"4706d491ce94b085","seat_id":"4636","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"3","column_num":"9","status":"available","update_time":0,"x_coord":"9","y_coord":"3","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"66128341c5e8a100","seat_id":"4689","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"9","column_num":"2","status":"available","update_time":0,"x_coord":"2","y_coord":"9","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"2e5fa297b620e511","seat_id":"4659","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"6","column_num":"2","status":"available","update_time":0,"x_coord":"2","y_coord":"6","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"3cd5dd8d466aa1c3","seat_id":"4633","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"3","column_num":"6","status":"available","update_time":0,"x_coord":"6","y_coord":"3","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"79d0b3d791c71a50","seat_id":"4643","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"4","column_num":"6","status":"available","update_time":0,"x_coord":"6","y_coord":"4","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"99719271081b3d68","seat_id":"4669","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"7","column_num":"2","status":"available","update_time":0,"x_coord":"2","y_coord":"7","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"eec40632c620608d","seat_id":"4638","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"4","column_num":"1","status":"available","update_time":0,"x_coord":"1","y_coord":"4","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"a847c38298afab6a","seat_id":"4629","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"3","column_num":"2","status":"available","update_time":0,"x_coord":"2","y_coord":"3","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"e2735e6dec0645e8","seat_id":"4709","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"2","column_num":"8","status":"available","update_time":0,"x_coord":"10","y_coord":"2","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"4847465964d6ecf4","seat_id":"4615","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"85","row_num":"1","column_num":"5","status":"sold","update_time":0,"x_coord":"6","y_coord":"1","bind_id":"0","seat_type_id":"5","seat_type_desc":"\\u4fdd\\u7559\\u5ea7\\u4f4d"}', '{"id":0,"seat_code":"bfd2e4b40bb39daa","seat_id":"4670","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"7","column_num":"3","status":"available","update_time":0,"x_coord":"3","y_coord":"7","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"00cd56ddc60aea83","seat_id":"4650","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"5","column_num":"3","status":"available","update_time":0,"x_coord":"3","y_coord":"5","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"1be17bef464b00b7","seat_id":"4634","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"3","column_num":"7","status":"available","update_time":0,"x_coord":"7","y_coord":"3","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"a43e2601e5d90189","seat_id":"4668","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"7","column_num":"1","status":"available","update_time":0,"x_coord":"1","y_coord":"7","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"3e2959fe5c77c567","seat_id":"4651","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"5","column_num":"4","status":"available","update_time":0,"x_coord":"4","y_coord":"5","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"df31aa12f7f1c975","seat_id":"4658","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"6","column_num":"1","status":"available","update_time":0,"x_coord":"1","y_coord":"6","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"439c5bf7fd7c8604","seat_id":"4627","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"2","column_num":"7","status":"available","update_time":0,"x_coord":"9","y_coord":"2","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"7d5c4ee6bc73be34","seat_id":"4690","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"9","column_num":"3","status":"available","update_time":0,"x_coord":"3","y_coord":"9","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"b36b8b5a5b17b42f","seat_id":"4708","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"1","column_num":"9","status":"available","update_time":0,"x_coord":"10","y_coord":"1","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"0d02e01c38293b2b","seat_id":"4652","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"5","column_num":"5","status":"available","update_time":0,"x_coord":"5","y_coord":"5","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"de0cab86b68374bf","seat_id":"4678","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"8","column_num":"1","status":"available","update_time":0,"x_coord":"1","y_coord":"8","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"057fde6f464c29c0","seat_id":"4621","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"2","column_num":"1","status":"available","update_time":0,"x_coord":"3","y_coord":"2","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"c5bbc1f457b73e6e","seat_id":"4662","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"6","column_num":"5","status":"available","update_time":0,"x_coord":"5","y_coord":"6","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"a663efff3fbb7197","seat_id":"4685","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"8","column_num":"8","status":"available","update_time":0,"x_coord":"8","y_coord":"8","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"5c85503f30522764","seat_id":"4646","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"4","column_num":"9","status":"available","update_time":0,"x_coord":"9","y_coord":"4","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"15917479ee315848","seat_id":"4635","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"3","column_num":"8","status":"available","update_time":0,"x_coord":"8","y_coord":"3","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"970641a7637524be","seat_id":"4628","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"3","column_num":"1","status":"available","update_time":0,"x_coord":"1","y_coord":"3","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"9798449470d01045","seat_id":"4655","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"5","column_num":"8","status":"available","update_time":0,"x_coord":"8","y_coord":"5","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"c905636b8d8b9619","seat_id":"4665","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"6","column_num":"8","status":"available","update_time":0,"x_coord":"8","y_coord":"6","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"024c22fcef2c6048","seat_id":"4687","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"8","column_num":"10","status":"available","update_time":0,"x_coord":"10","y_coord":"8","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"81ffef4e1407dcdb","seat_id":"4656","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"5","column_num":"9","status":"available","update_time":0,"x_coord":"9","y_coord":"5","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"3d47f1eca1e5019d","seat_id":"4701","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"10","column_num":"4","status":"available","update_time":0,"x_coord":"4","y_coord":"10","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"62d67aa0aea08959","seat_id":"4681","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"8","column_num":"4","status":"available","update_time":0,"x_coord":"4","y_coord":"8","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"67b7068b8cd2339b","seat_id":"4699","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"10","column_num":"2","status":"available","update_time":0,"x_coord":"2","y_coord":"10","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"e3a8ebc565e325a3","seat_id":"4691","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"9","column_num":"4","status":"available","update_time":0,"x_coord":"4","y_coord":"9","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"3689bb8a831ce1f0","seat_id":"4693","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"9","column_num":"6","status":"available","update_time":0,"x_coord":"6","y_coord":"9","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"8576a5769cef092b","seat_id":"4625","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"2","column_num":"5","status":"available","update_time":0,"x_coord":"7","y_coord":"2","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"2509de14202126e3","seat_id":"4623","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"2","column_num":"3","status":"available","update_time":0,"x_coord":"5","y_coord":"2","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"221d245b6761c3aa","seat_id":"4697","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"9","column_num":"10","status":"available","update_time":0,"x_coord":"10","y_coord":"9","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"dc8ee92a15210845","seat_id":"4703","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"10","column_num":"6","status":"available","update_time":0,"x_coord":"6","y_coord":"10","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"e44ad157413c4f10","seat_id":"4677","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"7","column_num":"10","status":"available","update_time":0,"x_coord":"10","y_coord":"7","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"ad05b0a86f38dd16","seat_id":"4661","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"6","column_num":"4","status":"available","update_time":0,"x_coord":"4","y_coord":"6","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"7e0785fde65f4bab","seat_id":"4674","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"7","column_num":"7","status":"available","update_time":0,"x_coord":"7","y_coord":"7","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"14e36394094c57b6","seat_id":"4617","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"1","column_num":"7","status":"available","update_time":0,"x_coord":"8","y_coord":"1","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"8ec4a04771a45cba","seat_id":"4612","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"3","row_num":"1","column_num":"2","status":"available","update_time":0,"x_coord":"3","y_coord":"1","bind_id":"1002","seat_type_id":"2","seat_type_desc":"\\u60c5\\u4fa3\\u5ea7"}', '{"id":0,"seat_code":"efff3b47bc4a3323","seat_id":"4649","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"5","column_num":"2","status":"available","update_time":0,"x_coord":"2","y_coord":"5","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"0a79aef489595fe7","seat_id":"4657","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"5","column_num":"10","status":"available","update_time":0,"x_coord":"10","y_coord":"5","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"00a7b4eeece06ade","seat_id":"4648","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"5","column_num":"1","status":"available","update_time":0,"x_coord":"1","y_coord":"5","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"4599b8e5343f29c0","seat_id":"4614","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"83","row_num":"1","column_num":"4","status":"available","update_time":0,"x_coord":"5","y_coord":"1","bind_id":"0","seat_type_id":"4","seat_type_desc":"\\u67dc\\u53f0\\u4e13\\u552e"}', '{"id":0,"seat_code":"cefe1b87983f4ed7","seat_id":"4663","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"6","column_num":"6","status":"available","update_time":0,"x_coord":"6","y_coord":"6","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"657d52eaee8b6bbc","seat_id":"4641","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"4","column_num":"4","status":"available","update_time":0,"x_coord":"4","y_coord":"4","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"5776c1ca8d028270","seat_id":"4611","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"3","row_num":"1","column_num":"1","status":"available","update_time":0,"x_coord":"2","y_coord":"1","bind_id":"1002","seat_type_id":"2","seat_type_desc":"\\u60c5\\u4fa3\\u5ea7"}', '{"id":0,"seat_code":"a459a6b2a9435654","seat_id":"4664","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"6","column_num":"7","status":"available","update_time":0,"x_coord":"7","y_coord":"6","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"f4f7441acdea42da","seat_id":"4630","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"3","column_num":"3","status":"available","update_time":0,"x_coord":"3","y_coord":"3","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"1a98f745304381f7","seat_id":"4680","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"8","column_num":"3","status":"available","update_time":0,"x_coord":"3","y_coord":"8","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"6b39eae33828191c","seat_id":"4694","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"9","column_num":"7","status":"available","update_time":0,"x_coord":"7","y_coord":"9","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"f635d10e74f9a69d","seat_id":"4644","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"4","column_num":"7","status":"available","update_time":0,"x_coord":"7","y_coord":"4","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"a31f075a2cf7b092","seat_id":"4700","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"10","column_num":"3","status":"available","update_time":0,"x_coord":"3","y_coord":"10","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"bd8f35c03f85aac9","seat_id":"4653","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"5","column_num":"6","status":"available","update_time":0,"x_coord":"6","y_coord":"5","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"a3872a9493b2046b","seat_id":"4683","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"8","column_num":"6","status":"available","update_time":0,"x_coord":"6","y_coord":"8","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"9602c03d67ec36e4","seat_id":"4695","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"9","column_num":"8","status":"available","update_time":0,"x_coord":"8","y_coord":"9","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"861101c39fa62a12","seat_id":"4682","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"8","column_num":"5","status":"available","update_time":0,"x_coord":"5","y_coord":"8","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"ce5aea07ddd3bf88","seat_id":"4706","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"10","column_num":"9","status":"available","update_time":0,"x_coord":"9","y_coord":"10","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"3f45161f1017e7e2","seat_id":"4632","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"3","column_num":"5","status":"available","update_time":0,"x_coord":"5","y_coord":"3","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}', '{"id":0,"seat_code":"f089d233caff74ea","seat_id":"4705","session_code":"15bb78b0d1d24bbb","session_id":"6089","cinema_code":"10000142","cinema_id":"42","group_id":"78","row_num":"10","column_num":"8","status":"available","update_time":0,"x_coord":"8","y_coord":"10","bind_id":"0","seat_type_id":"1","seat_type_desc":"\\u666e\\u901a\\u5ea7"}']

    b = List()._sort_dictlist(a1,"seat_id")
    print b
