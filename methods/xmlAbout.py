#coding:utf-8

try:
    import xmltodict
except ImportError:
    from TicketBusinessLibrary.libs import xmltodict



class XmlAbout():
    def __init__(self):
        pass

    def _xml_to_dict(self,xml_resp,order_by='',pass_tag=[],*level_tag_names):
        '''
        将XML型的响应结果转化为字典，level_tag_names为
        需要获取的XML的层级,按照order_by的值进行排序,默认可不填。
        pass_tag为需要忽略的tag列表
        '''
        convert_string = xmltodict.parse(xml_resp)
        print convert_string


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
        </Cinema>    </Cinemas>
</GetCinemaResult>
"""

    a = XmlAbout()._xml_to_dict(xml1)
    #print a

