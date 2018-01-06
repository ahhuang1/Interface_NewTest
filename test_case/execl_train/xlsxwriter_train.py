#！/usr/bin/env.python
#coding:utf-8
#写入excel操作

import xlsxwriter
import datetime
#创建excel文件

workbook = xlsxwriter.Workbook('test1.xlsx')#创建文件
worksheet = workbook.add_worksheet('test1')#创建sheet，清空文件

#2.特定单元格写入

worksheet.write('A1','黄爱华')
worksheet.write(1,0,'下标进行写入')
worksheet.write(0,1,32)

worksheet.set_row(0,40)#设置好行属性
worksheet.set_column('A:A',20)#设置列属性\

#写入数字和函数
worksheet.write(0,1,32)
worksheet.write(1,1,35.5)
worksheet.write(2,1,'=sum(B1:B2)')

#写入日期
#worksheet.write(0,2,datetime.datetime.strptime('2017-11-11','%Y-%m-%d'),workbook.add_format({'num.format':'yyyy-mm-dd'}))

#插入图片
worksheet.insert_image(0,4,'sfdfa.jpg')
worksheet.insert_image(0,4,'sfdfa.jpg',{'x_scale':0.2,'y_scale':0.2,'url':'www.baidu.com'})

#批量写入单元格
worksheet.write_column('A22',[1,2,3,4])#列写入，从A22写起
worksheet.write_row('A21',[5,6,7,8])#行写入，从A21写起

#合并单元格写入
worksheet.merge_range(4,0,5,2,'黄爱华')

#写入图表
workbook.add_chart()

#关闭文件
workbook.close()