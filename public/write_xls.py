import xlrd
from xlutils.copy import copy

#xls文件写入模块
class ExcelUtil_write(object):
    def __init__(self, excelPath):
        self.data = xlrd.open_workbook(excelPath,formatting_info=True)
        self.newdata = copy(self.data)


    def new_tabe(self,sheetindex):
        newtable = self.newdata.get_sheet(sheetindex)
        newdata = self.newdata
        return newtable,newdata

    def save_excel(self):
        return self.newdata
