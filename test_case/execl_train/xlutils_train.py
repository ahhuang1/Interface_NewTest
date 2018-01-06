#！/usr/bin/env.python
#coding:utf-8
import xlutils.copy
import xlrd
#xlrd打开文件
xl = xlrd.open_workbook('test1.xlsx')
#复制xl文件
workbook = xlutils.copy.copy(xl)
#通过get_sheet()获取的sheet
worksheet = workbook.get_sheet(0)
#修改操作
worksheet.write(0,0,'changed')
#另存
workbook.save(r'xlutils_save.xls')#不会把格式复制过来；只支持xls


