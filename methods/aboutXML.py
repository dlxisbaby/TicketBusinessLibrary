#coding:utf-8

try:
    import xmltodict
except ImportError:
    from TicketBusinessLibrary.libs import xmltodict

import sys,operator
reload(sys)
sys.setdefaultencoding("utf8")
from collections import OrderedDict

import xml.dom.minidom
from xml.dom.minidom import parse

class Xml():
    def __init__(self,xml_code):
        self.xml_code = xml_code

    def _xml_to_dict_list(self,*tag_level_names):
        '''
        将xml响应转化为字典列表形式，用户结果对比
        :param xml_code:xml响应
        :param tag_level_names: 层级名称
        :return:
        '''
        convert_string = dict(xmltodict.parse(self.xml_code))
        length = len(tag_level_names)
        final_list = []
        for i in range(length):
            convert_string = convert_string[tag_level_names[i]]
            if length == 1:
                convert_string.pop("@xmlns:xsi")
                convert_string.pop("@xmlns:xsd")
        if type(convert_string) == OrderedDict:
            convert_string = [convert_string]
        for i in convert_string:
            final_dict = dict(i)
            final_list.append(final_dict)
        return Sort(final_list)

    def _get_xml_resp_code_by_tag(self,tag_name):
        '''
        解析返回的XML，返回所输入标签的内容\n
        如:<tag_name>123</tag_name>,则返回123\n
        '''
        xml_data = xml.dom.minidom.parseString(self.xml_code)
        Results = xml_data.getElementsByTagName(tag_name)
        for result in Results:
            if len(result.childNodes) != 0:
                return result.childNodes[0].data
            else:
                return ''

    def _get_xml_resp_code_by_unique(self,tag_name,unique):
        '''
        解析返回的XML，返回tag_name标签的下级，unique_name
        标签值的列表
        '''
        xml_data = xml.dom.minidom.parseString(self.xml_code)
        Results = xml_data.getElementsByTagName(tag_name)
        value_list = []
        for result in Results:
            if result.getElementsByTagName(unique)[0].childNodes[0].data !=None:
                value_list.append(result.getElementsByTagName(unique)[0].childNodes[0].data)
                continue
            else:
                break
        return value_list

    def _get_xml_resp_code_by_uni_name_and_value(self,tag_name,uni_name,uni_value,hope_name):
        '''
        解析返回的XML，返回hope_name的值\
        uni_name为唯一标识标签名，uni_value为唯一标识的值\
        hope_name为与uni_name同级的标签的值\n
        '''
        xml_data = xml.dom.minidom.parseString(self.xml_code)
        Results = xml_data.getElementsByTagName(tag_name)
        for result in Results:
            uni_id = result.getElementsByTagName(uni_name)[0].childNodes[0].data
            if str(uni_id) == str(uni_value):
                return result.getElementsByTagName(hope_name)[0].childNodes[0].data
                break

class Handle():
    def __init__(self,dict_list):
        self.dict_list = dict_list

    def _except_pass_tags(self,pass_tag_list=[]):
        '''
        去除不参与对比的标签（包括弃用、值为空等）
        :param pass_tag_list: 不参与对比标签的列表
        :return:
        '''
        if len(pass_tag_list) != 0:
            for i in self.dict_list:
                for j in pass_tag_list:
                    i.pop(j)
        return self.dict_list

class Sort():
    def __init__(self,dict_list):
        self.dict_list = dict_list

    def _order_by(self,key=''):
        '''
        使用key对字典列表进行排序
        :param key:排序依据的标签
        :return:
        '''
        if key != '':
            for i in self.dict_list:
                i[key] = int(i[key])
            self.dict_list.sort(key=operator.itemgetter(key))
            for i in self.dict_list:
                i[key] = str(i[key]).decode("utf-8")
        return Handle(self.dict_list)


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
    pass_tag_list = ['CreateDate']
    key = ''
    a = Xml()._get_xml_resp_code_by_uni_name_and_value(xml1,"Cinema","CinemaNo","41","CinemaName")
    print a


