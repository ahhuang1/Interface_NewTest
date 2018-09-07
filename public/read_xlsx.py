#！/usr/bin/env.python
#coding:utf-8

import xlrd

#xlsx和xls文件的读取
class ExcelUtil(object):
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)

        # get titles
        self.row = self.table.row_values(0)

        # get rows number
        self.rowNum = self.table.nrows

        # get columns number
        self.colNum = self.table.ncols

        # the current column
        self.curRowNo = 1

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

if __name__ == '__main__':
    excel = ExcelUtil(r'D:\Interface_Test_Training\test_data\test_data.xls', 'test').next()

    CaseId = excel[0]['CaseId']
    print(CaseId)
    for i in excel:

        if i['CaseId'] == CaseId:
            print(4)
            print(excel.index(i))