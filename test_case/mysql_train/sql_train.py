#！/usr/bin/env.python
#coding:utf-8

import pymysql
from public import Config

#1.创建连接、游标创建
conn = pymysql.connect(**Config.sql_conn_dict)
cur = conn.cursor()

#2.数据库操作
sql = 'select * from student'
cur.execute(sql)
cur.scrool(0,mode = 'absolute')#将游标移动回初始位置
print(cur.fetchone())
print(cur.fetchone())
print(cur.execute(sql))#显示影响的行数

#查询
code = ('1','2','3')
sql = 'select * from student where code = %s'
cur.executemany(sql,code)#执行多个参数的sql操作
print(cur.fetchall())

#增删改
code = (('a','18','man'),('b','19','woman'))
sql = 'update student set name = %s where age= %s and sex = %s'
cur.executemany(sql,code)
conn.commit()

#3.关闭连接
cur.close()
conn.close()