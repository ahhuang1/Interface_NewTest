#！/usr/bin/env.python
#coding:utf-8

#测试url的根路径
def url():
    #url = 'http://httpbin.org/'
    url = 'http://210.21.217.195:7001/DLMiddleware_bs-deploy/restful/'
    #url = 'http://180.166.172.126:8080/huatai/midlogin/'
    return url

login_url = 'http://210.21.217.195:7001/DLMiddleware_bs-deploy/restful/deploy/user/mlogin'

#mock模块开关
def mock_open():
    open = 'ON'
    return  open

#数据库连接串
sql_conn_dict = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'passwd':'123456',
    'db':'test',
    'charset':'utf-8'
}