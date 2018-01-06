#！/usr/bin/env.python
#coding:utf-8

#读取excel

import os
import xlrd
from datetime import date,datetime

newpath = os.chdir(r'D:\Interface_Test_Training\test_case\execl_train')
filename = '企业课题来源一览表-黄爱华.xlsx'
file = os.path.join(os.getcwd(),filename)
#1.打开文件
xl = xlrd.open_workbook(file)
#2.获取sheet
print(xl.sheet_names())#获取sheet的名字
print(xl.sheets())#获取sheet的对象
print(xl.nsheets)#获取sheet的数量
print(xl.sheet_by_name('Sheet2'))#通过sheet的名字获取
print(xl.sheet_by_index(0))#通过下标获取
#3.获取sheet内的汇总数据
table1 = xl.sheet_by_name('Sheet1')
# print(table1.name)#获取表名
# print(table1.nrows)#获取表的行数
# print(table1.ncols)#获取表的列数
#4.单元格批量读取
print(table1.row_values(0))#合并单元格，首行显示值，其他为空
# print(table1.row(0))#显示行数的类型以及相应的值
# print(table1.row_types(0))#显示行数的类型
print(table1.col_values(0,0,2))
print(table1.row_slice(0,0,2))
print(table1.row_types(0,0,2))
#5.特定单元格读取
#取值
print()
print(table1.cell(1,2).value)
print(table1.cell_value(1,2))
print(table1.row(1)[2].value)
#取类型
print()
print(table1.cell(1,2).ctype)
print(table1.cell_type(1,2))
print(table1.row(1)[2].ctype)
#6.常用技巧：（0,0）转换成A1
print()
print(xlrd.cellname(0,0))
print(xlrd.cellnameabs(0,2))
print(xlrd.colname(30))

def read_excel(table,row,col):
    name = table.cell_value(row,col)
    type = table.cell_type(row,col)
    if type ==0:
        name = "'"
    elif type ==1:
        name = name
    elif type ==2 and name % 1 ==0:
        name = int(name)
    elif type ==3:
        #方法1 转换为日期时间
        # date_value = xlrd.xldate.xldate_as_datetime(name,0)
        # name = date_value
        #方法2转换为元组
        date_value = xlrd.xldate_as_tuple(name,0)
        name = datetime(*date_value).strftime('%Y/%m/%d %H%M%S')
    elif type ==4:
        name = True if name ==1 else False
    return name

#7.获取表格内不同类型的name
print()
print(table1.cell_value(1,0))#字符
print(table1.cell_type(1,0))
print(read_excel(table1,1,0))
print(table1.cell_value(2,0))#数字
print(table1.cell_type(2,0))
print(read_excel(table1,2,0))
print(table1.cell_value(0,1))#空
print(table1.cell_type(0,1))
print(read_excel(table1,0,1))
print(table1.cell_value(0,9))#日期
print(table1.cell_type(0,9))
print(read_excel(table1,0,9))
print(table1.cell_value(0,10))#布尔
print(table1.cell_type(0,10))
print(read_excel(table1,0,10))