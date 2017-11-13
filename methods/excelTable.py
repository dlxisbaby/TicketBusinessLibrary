#coding:utf-8

from robot.api import logger

try:
    import xlrd
except ImportError:
    from TicketBusinessLibrary.libs import xlrd

class ExcelTable():
    def __init__(self):
        pass

    def _readExcel(self,file_path,sheet,row_num):
        datas = xlrd.open_workbook(file_path)
        data = datas.sheet_by_name(sheet).row_values(row_num)
        return data

if __name__ == "__main__":

    print ExcelTable()._readExcel(u"影院相关.xlsx",u"获取影院信息",row_num=2)

