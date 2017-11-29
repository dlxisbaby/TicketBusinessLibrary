#coding:utf-8


import sys
reload(sys)
sys.setdefaultencoding('utf8')

from TicketBusinessLibrary.methods.aboutDB import Database,Redis
from TicketBusinessLibrary.methods.aboutXML import *
from TicketBusinessLibrary.methods.aboutString import String
from TicketBusinessLibrary.methods.aboutList import List
from TicketBusinessLibrary.methods.aboutTime import Time
from TicketBusinessLibrary.methods.aboutFile import File
from TicketBusinessLibrary.methods.aboutNumber import Number
from TicketBusinessLibrary.methods.aboutDict import Dict
from TicketBusinessLibrary import config

from robot.api import logger

class TicketKeywords():
    def __init__(self):
        pass

    def dlx_select_142database_by_sql(self,sql,db_name=config.cinema_info["mysql_db"],ip=config.cinema_info["ip"],port=3306,user=config.cinema_info["mysql_user"],passwd=config.cinema_info["mysql_passwd"]):
        '''
        使用自写sql查询任意服务器的数据库,返回列表\n
        :param db_name: 数据吗名称\n
        :param sql: 查询语句\n
        :param ip: IP地址\n
        :param port: 端口\n
        :param user: 用户名\n
        :param passwd: 密码\n
        '''
        datas = Database(ip,int(port),user,passwd).DB_select_by_sql(db_name,sql)
        if type(datas[0]) == tuple and len(datas[0]) <= 1:
            data_list = []
            for i in datas:
                data_list.append(i[0])
            return data_list
        else:
            return datas

    def dlx_select_Middatabase_by_sql(self,sql,db_name=config.mid_info["mysql_db"],ip=config.mid_info["ip"],port=3306,user=config.mid_info["mysql_user"],passwd=config.mid_info["mysql_passwd"]):
        '''
        使用自写sql查询任意服务器的数据库,返回列表\n
        :param db_name: 数据吗名称\n
        :param sql: 查询语句\n
        :param ip: IP地址\n
        :param port: 端口\n
        :param user: 用户名\n
        :param passwd: 密码\n
        '''
        datas = Database(ip,int(port),user,passwd).DB_select_by_sql(db_name,sql)
        if type(datas[0]) == tuple and len(datas[0]) <= 1:
            data_list = []
            for i in datas:
                data_list.append(i[0])
            return data_list
        else:
            return datas

    def dlx_select_database_by_sql(self,sql,db_name,ip,port,user,passwd):
        '''
        使用自写sql查询任意服务器的数据库,返回列表\n
        :param db_name: 数据吗名称\n
        :param sql: 查询语句\n
        :param ip: IP地址\n
        :param port: 端口\n
        :param user: 用户名\n
        :param passwd: 密码\n
        '''
        datas = Database(ip,int(port),user,passwd).DB_select_by_sql(db_name,sql)
        if type(datas[0]) == tuple and len(datas[0]) <= 1:
            data_list = []
            for i in datas:
                data_list.append(i[0])
                logger.info(i[0])
            return data_list
        else:
            return datas

    def dlx_assert_two_result(self,expect,actual,msg=''):
        '''
        验证预期结果与实际结果是否相同\n
        :param expect: 预期结果\n
        :param actual: 实际结果\n
        '''

        if expect == actual:
            logger.info(u"预期与实际结果相同")
        else:
            logger.info(u"预期结果为：{0}".format(expect))
            logger.info(u"实际结果为：{0}".format(actual))
            if msg == '':
                raise AssertionError(u"预期与实际结果不同")
            else:
                raise AssertionError(msg)


    def dlx_assert_xml_resp_code(self,expect,actual):
        '''
        验证预期结果与实际结果是否相同\n
        :param expect: 预期结果\n
        :param actual: 实际结果\n
        '''

        if expect == actual:
            logger.info(u"预期与实际状态相同")
        else:
            logger.info(u"预期状态为：{0}\"{1}\"".format(expect,config.resp_code[expect]))
            logger.info(u"实际状态为：{0}\"{1}\"".format(actual,config.resp_code[actual]))
            raise AssertionError(u"返回的状态与预期不相符")

    def dlx_xml_to_dictlist(self,xml_code,order_by='',pass_tag_list=[],*level_tag_names):
        '''
        将xml响应转化为字典列表
        :param xml_code: xml响应
        :param pass_tag_list: 忽略的标签列表
        :param order_by: 排序的标签
        :param level_tag_names: xml响应的层级标签
        '''
        dict_list = Xml(xml_code)._xml_to_dict_list(*level_tag_names)._order_by(order_by)._except_pass_tags(pass_tag_list)
        return Dict()._orderdict_to_dict(dict_list)

    def dlx_check_contain_chinese(self,check_str):
        '''
        检查字符串是否包含中文
        :param check_str:被检查得字符串
        '''
        return String._check_str_contain_chinese(check_str)

    def dlx_repeated_key_to_post_data(self,num,key_name,from_list):
        '''
        将列表转化为post类型的数据
        '''
        string_list = str(from_list)
        string = ''
        if ",)" in string_list:
            for i in from_list[:int(num)]:
                string = string + "{0}={1}&".format(key_name,i[0])
        else:
            for i in from_list[:int(num)]:
                string = string + "{0}={1}&".format(key_name,i)
        return string[:-1]

    def dlx_add_dict_to_list(self,num,**dict_key_value):
        '''
        将从数据库中查询出的字典列表转换为可对比的字典列表
        如：
        dict1 = {'a':[1,3,5,7,9],'b':[2,4,6,8,10]}
        如果num=3，则转化为:
        [{'a':1,'b':2},{'a':3,'b':4},{'a':5,'b':6}]
        '''
        num_list = range(0,int(num))
        expect_list = []
        for j in num_list:
            dict2 = {}
            for i in dict_key_value:
                if ',)' in str(dict_key_value[i]):
                    if type(dict_key_value[i][j][0]) == type(unicode()):
                        if mytool().dlx_check_contain_chinese(dict_key_value[i][j][0]) == True:
                            dict2[i.encode("utf8")] = dict_key_value[i][j][0]
                        else:
                            dict2[i.encode("utf8")] = dict_key_value[i][j][0].encode("utf8")
                    elif type(dict_key_value[i][j][0]) == type(int()) or type(dict_key_value[i][j][0]) == type(float()):
                        dict2[i.encode("utf8")] = str(dict_key_value[i][j][0]).encode("utf8")
                    else:
                        dict2[i.encode("utf8")] = str(dict_key_value[i][j][0]).encode("utf8")
                else:
                    if type(dict_key_value[i][j]) == type(unicode()):
                        if mytool().dlx_check_contain_chinese(dict_key_value[i][j]) == True:
                            dict2[i.encode("utf8")] = dict_key_value[i][j]
                        else:
                            dict2[i.encode("utf8")] = dict_key_value[i][j].encode("utf8")
                    elif type(dict_key_value[i][j]) == type(int()) or type(dict_key_value[i][j]) == type(float()):
                        dict2[i.encode("utf8")] = str(dict_key_value[i][j]).encode("utf8")
                    else:
                        dict2[i.encode("utf8")] = str(dict_key_value[i][j]).encode("utf8")
            expect_list.append(dict2)
        return expect_list

    def dlx_select_db_json_to_tuple(self,DB_list):
        '''
        将从数据库中查询出来列表（json）转化为元组，作为IN关键字后的条件
        如：
        [(u'["S20160927766190","S20160927159910"]',), (u'["S20160927766190","S20160927825520","S20160927936647","S20160927159910","P20160927764039"]',), (u'["P20161018158611"]',)]
        转化为：
        (u'S20160927766190', u'S20160927159910', u'S20160927766190', u'S20160927825520', u'S20160927936647', u'S20160927159910', u'P20160927764039', u'P20161018158611')
        '''
        final_list = []
        for i in DB_list:
            string  = i[0][2:-2]
            list1 = string.split('","')
            for j in list1:
                final_list.append(j.encode("utf8"))
        return tuple(final_list)

    def dlx_get_length_equal_n_list(self,num,list_value):
        '''
        num为3，list_value为group
        则生成一个列表为[group,group,group]
        '''
        list1 = []
        num_list = range(0,int(num))
        for i in num_list:
            list1.append(list_value)
        return list1

    def dlx_list_subtract_list(self,list1,list2):
        '''
        列表1减去列表2，返回新的列表
        '''
        for i in list2:
            list1.remove(i)
        return list1

    def dlx_db_list_to_standard_list(self,db_list,mode="1"):
        '''
        将查询数据库的列表，如：
        [(1,), (3,), (15,), (16,), (17,), (18,), (19,), (20,)]
        转化为标准列表
        [1, 3, 15, 16, 17, 18, 19, 20](mode=1时)
        [u'1',u'3',u'15',u'17',u'18',u'19',u'20'](mode=2时)
        '''
        return List()._db_list_to_standard_list(db_list,mode="1")

    def dlx_get_current_unix_time_string(self):
        '''
        获得当前时间的unix时间戳字符串
        '''
        return Time()._get_current_unix_time()

    def dlx_md5_32_lowercase(self,string):
        '''
        对字符串进行32位小写的MD5加密
        '''
        return String()._md5_32_lowercase(string)

    def dlx_get_xml_resp_code(self,xml_resp,tag_name,uni_name="",uni_value="",hope_name=""):
        '''
        解析返回的XML，返回所输入标签的内容\n
        1、后面3个参数都为空时，如:<tag_name>123</tag_name>,则返回123\n
        2、如果后面3个参数同时不为空，则返回hope_name的值\
        uni_name为唯一标识标签名，uni_value为唯一标识的值\
        hope_name为与uni_name同级的标签的值\n
        3、如果只有后面2个参数为空，则返回tag_name标签的下级，uni_name
        标签值的列表
        '''
        if uni_value == '' and hope_name == '' and uni_name == '':
            return Xml(xml_resp)._get_xml_resp_code_by_tag(tag_name)
        elif uni_value == '' and hope_name == '':
            return Xml(xml_resp)._get_xml_resp_code_by_unique(tag_name,uni_name)
        elif uni_value != '' and hope_name != '' and uni_name != '':
            return Xml(xml_resp)._get_xml_resp_code_by_uni_name_and_value(tag_name,uni_name,uni_value,hope_name)

    def dlx_sql_result_to_dictlist(self,tag_name_list,*tag_value_lists):
        '''
        tag_value_lists = [list1,list2,list3,……]\n
        tag_value_lists的长度应等于tag_name_list的长度\n
        将tag_value_lists中每个列表的第一个值赋值给tag_name_list列表，\
        形成字典，以此类推，最后生成值为字典的列表\n
        '''
        if type(tag_value_lists[0]) == list or type(tag_value_lists[0]) == tuple:
            return List()._sql_list_to_dict_list(tag_name_list,*tag_value_lists)
        else:
            return List()._sql_single_to_dict(tag_name_list,*tag_value_lists)

    def dlx_get_php_config_key_value(self,server_ip,remote_path,keyname):
        '''
        获取服务器中config.php中的keyname的值
        '''
        return File()._get_php_config_key_value(server_ip,remote_path,keyname)

    """
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
    """
    def dlx_make_list_to_dict_list(self,up_level,level_name_list,*level_value_list):
        '''
        生成一个字典列表
        :param up_level: 上级名称
        :param level_name_list: 层级名称列表level_name_list=[u'FilmNo', u'FilmName', u'FilmType', u'Language']
        :param level_value_list: 层级值列表，需要与层级名称列表中的值一一对应FilmNo_list,FilmName_list,FilmType_list,Language_list
        '''
        return Dict()._make_list_to_dict_list(up_level,level_name_list,*level_value_list)

    def dlx_contact_two_dict_list(self,list_main,list_order,key_name):
        '''
        连接2个字典列表，key_name是list_main中的字典需要新加的key
        '''
        return List()._contact_two_dict_list(list_main,list_order,key_name)

    def dlx_get_value_list_from_redis(self,cinema_code,session_code,order_by_key):
        '''
        从redis中获取座位数据
        '''
        return Redis()._get_value_list_from_redis(cinema_code,session_code,order_by_key)

    def dlx_convert_dict_list_to_float(self,dict_list,fields):
        '''
        将dict_list中的字典的字段值转化为float类型
        '''
        return Number()._convert_dict_list_to_float(dict_list,fields)

    def dlx_keep_significant_digit(self,obj):
        '''
        使一个浮点型数字，或者列表中、元组中的浮点型数字
        取消小数点后的无效0
        '''
        if type(obj) == float:
            return Number()._remove_zero_from_float(obj)
        elif type(obj) == list or type(obj) == tuple:
            return Number()._remove_zero_from_list_or_tuple(obj)
        else:
            return obj

    def dlx_make_string_for_sql(self,list_obj):
        '''
        转换一个列表给数据库的in关键字使用
        '''
        return String()._make_string_for_sql(list_obj)

    def dlx_remove_float_end_zero(self,list_begin):
        '''
        消除列表里面float类型尾部的0
        '''
        return List()._remove_float_end_zero(list_begin)

    def dlx_get_n_length_same_list(self,n,value,mode=1):
        '''
        N为3，value为None\n
        mode为1生成[u'None',u'None',u'None']\n
        mode为2生成['None','None','None']\n
        mode为3生成[None,None,None]\n
        :param n: 列表长度\n
        :param value: 列表的值\n
        '''
        return List()._get_n_length_same_value_list(n,value,mode)


if __name__ == "__main__":
    xml1 ="""<?xml version="1.0"?>
    <GetCinemaResult xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <ResultCode>0</ResultCode>
        <Cinemas>
            <Cinema>
                <CinemaNo>40</CinemaNo>
                <CinemaName>北京155</CinemaName>
                <CinemaCode>10000155</CinemaCode>
                <CityNo></CityNo>
                <CreateDate></CreateDate>
            </Cinema><Cinema>
                <CinemaNo>41</CinemaNo>
                <CinemaName>137测试服务器</CinemaName>
                <CinemaCode>10000137</CinemaCode>
                <CityNo></CityNo>
                <CreateDate></CreateDate>
            </Cinema><Cinema>
                <CinemaNo>42</CinemaNo>
                <CinemaName>10000142影院</CinemaName>
                <CinemaCode>10000142</CinemaCode>
                <CityNo></CityNo>
                <CreateDate></CreateDate>
            </Cinema>    
        </Cinemas>
    </GetCinemaResult>
"""

    xml2 = """<?xml version="1.0"?>
<GetCinemaSessionResult xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <ResultCode>0</ResultCode>
    <Sessions>
        <Session>
            <SessionNo>6074</SessionNo>
            <SessionDate>2017-11-27</SessionDate>
            <StartTime>15:45</StartTime>
            <TotalTime>120</TotalTime>
            <Consecutive>0</Consecutive>
            <FilmCount>1</FilmCount>
            <Films>
                <Film>
                    <FilmNo>458</FilmNo>
                    <FilmName>狂兽(2D) </FilmName>
                    <FilmType>2d</FilmType>
                    <Language>cn</Language>
                </Film>            
            </Films>
            <ScreenNo>5</ScreenNo>
            <ScreenType>normal</ScreenType>
            <CinemaNo>42</CinemaNo>
            <AppPrice>69</AppPrice>
            <SettlementPrice>60.00</SettlementPrice>            
            <StandartPrice>60.00</StandartPrice>
            <LowestPrice>20.00</LowestPrice>
            <Fee>9.00</Fee>
            <Type>2D</Type>
            <Status>1</Status>
        </Session>
        <Session>
            <SessionNo>6075</SessionNo>
            <SessionDate>2017-11-27</SessionDate>
            <StartTime>15:55</StartTime>
            <TotalTime>90</TotalTime>
            <Consecutive>0</Consecutive>
            <FilmCount>1</FilmCount>
            <Films>
                <Film>
                    <FilmNo>438</FilmNo>
                    <FilmName>分类细化(中国巨幕3D22) </FilmName>
                    <FilmType>dmax3d</FilmType>
                    <Language>cn</Language>
                </Film>            
            </Films>
            <ScreenNo>9</ScreenNo>
            <ScreenType>cmax</ScreenType>
            <CinemaNo>42</CinemaNo>
            <AppPrice>59</AppPrice>
            <SettlementPrice>50.00</SettlementPrice>            
            <StandartPrice>50.00</StandartPrice>
            <LowestPrice>45.00</LowestPrice>
            <Fee>9.00</Fee>
            <Type>2D</Type>
            <Status>1</Status>
        </Session>
        <Session>
            <SessionNo>6076</SessionNo>
            <SessionDate>2017-11-27</SessionDate>
            <StartTime>18:00</StartTime>
            <TotalTime>120</TotalTime>
            <Consecutive>0</Consecutive>
            <FilmCount>1</FilmCount>
            <Films>
                <Film>
                    <FilmNo>183</FilmNo>
                    <FilmName>湄公河行动(中国巨幕) </FilmName>
                    <FilmType>3d</FilmType>
                    <Language>cn</Language>
                </Film>            
            </Films>
            <ScreenNo>5</ScreenNo>
            <ScreenType>normal</ScreenType>
            <CinemaNo>42</CinemaNo>
            <AppPrice>89</AppPrice>
            <SettlementPrice>80.00</SettlementPrice>            
            <StandartPrice>80.00</StandartPrice>
            <LowestPrice>0.01</LowestPrice>
            <Fee>9.00</Fee>
            <Type>2D</Type>
            <Status>1</Status>
        </Session>
        <Session>
            <SessionNo>6077</SessionNo>
            <SessionDate>2017-11-27</SessionDate>
            <StartTime>20:10</StartTime>
            <TotalTime>160</TotalTime>
            <Consecutive>0</Consecutive>
            <FilmCount>1</FilmCount>
            <Films>
                <Film>
                    <FilmNo>439</FilmNo>
                    <FilmName>九一八(影展观摩片) </FilmName>
                    <FilmType>view</FilmType>
                    <Language>cn</Language>
                </Film>            
            </Films>
            <ScreenNo>5</ScreenNo>
            <ScreenType>normal</ScreenType>
            <CinemaNo>42</CinemaNo>
            <AppPrice>59</AppPrice>
            <SettlementPrice>50.00</SettlementPrice>            
            <StandartPrice>50.00</StandartPrice>
            <LowestPrice>5.00</LowestPrice>
            <Fee>9.00</Fee>
            <Type>2D</Type>
            <Status>1</Status>
        </Session>    
    </Sessions>
</GetCinemaSessionResult>
"""
    a = [1.20,2.3,3.40,4.00,40.00]


    b = TicketKeywords().dlx_get_value_list_from_redis("10000142","d02dd5c319c24af9","seat_id")
    print b
    print len(b)



