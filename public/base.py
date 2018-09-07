#！/usr/bin/env.python
#coding:utf-8
from public import Config
from public import HttpService

def get_url(Endpoint):
    host = Config.url()
    endpoint = Endpoint
    url = ''.join([host, endpoint])
    return url

def get_response(url,Method,cookies_session,**DataALL):

    if Method=='get':
        resp = HttpService.MyHTTP().get(url,cookies_session, **DataALL)
    elif Method == 'post':
        resp = HttpService.MyHTTP().post(url,cookies_session, **DataALL)
    elif Method == 'delete':
        resp = HttpService.MyHTTP().delete(url,cookies_session, **DataALL)

    return resp


def get_mock_status():
    mock_status = Config.mock_open()
    return mock_status

#比较字典
def dict_bijiao(dict1,dict2):
    for key,value in dict1.items():
        try:
            if key in dict2 and dict2.get(key) == value:
                pass
            else:
                return False
                break
        except:
            return False
    return True

#获取excel行数
def get_row(list,value):
    for i in list:
        if i['CaseId'] == value:
            return list.index(i) + 1

#md5加密
import hashlib

def md5_pwd(num):
    m = hashlib.md5()
    m.update(num.encode('utf-8'))
    return m.hexdigest()

