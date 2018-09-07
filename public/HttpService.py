#！/usr/bin/env.python
#coding:utf-8

import requests
import json
from public import Config


class MyHTTP(object):
    def __init__(self):
        self.url = Config.url()
        self.my_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
        }

    def get(self,url,cookies_session,**DataALL):
        params = DataALL.get('params')
        headers = self.my_headers
        # self.url = base.get_url(data['endpoint'])
        # DataALL = eval(data['Params'])
        # print(type(DataALL))
        # Method = data['RequestSend']
        try:
            resp = requests.get(url,params=params,headers=headers,cookies=cookies_session,timeout = 3)
            text = resp.json()
            return text
        except Exception as e:
            print('GET错误%s'%e)

    def post(self,url,cookies_session,**DataALL):
        params = DataALL.get('params')
        headers = self.my_headers
        data = DataALL.get('data')
        json = DataALL.get('json')
        cookies = cookies_session
        if json:
            headers["Content-Type"] = "application/json;charset=UTF-8"
        try:
            resp = requests.post(url,params=params,headers=headers,data=data,json=json,cookies=cookies_session,timeout=3)
            text = resp.json()
            return text
        except Exception as e:
            print('POST错误%s' % e)
            return resp.text
