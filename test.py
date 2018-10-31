#！/usr/bin/env.python
#coding:utf-8

import requests
import hashlib

# def md5_pwd(num):
#     m = hashlib.md5()
#     m.update(num.encode('utf-8'))
#     return m.hexdigest()
#
# url='http://210.21.217.195:7001/DLMiddleware_bs-deploy/restful/deploy/user/mlogin'
# data = {'username':'huafeng','password':md5_pwd('000000')}
# session = requests.session()
# rep = session.post(url,data=data)
# cookies_session = rep.cookies.get_dict()
# print(rep.json())
# print(rep.cookies.get_dict())
# url1='http://210.21.217.195:7001/DLMiddleware_bs-deploy/restful/deploy/manager/mod'
# json = {
#     'managername': '蔡滨',
#     'basecount': '8',
#     'managerid': 'caibin'
# }
# rep = requests.post(url1,data=json,cookies=cookies_session)
# print(rep.json())
# print(rep.cookies.get_dict())
# rep1 = requests.post(url1,data=json)
# print(rep1.text)

#递归
def dict_bijiao(dict1,dict2):
    for key,value in dict1.items():
        if key in dict2.keys():
            if isinstance(value,dict):
                # dict_bijiao(value,dict2.get(key))
                if not dict_bijiao(value,dict2.get(key)):
                    return False
            else:
                if dict2.get(key) == value:
                    pass
                else:
                    return False
        else:
            return False
    return True


dict2 = {'a':'1',
        'b':'2',
        'c':{'A':'12',
             'B':'34',
             'C':{'q':'123',
                  'daf':'123',
                  '123':{'zcxv':'123',
                         'asdf':'321'},
                  },
             },
        }

dict1 = {
    'c':{
        'A':'12',
        'C':{'q':'123',
             '123':{
                 'zcxv':'123',
                 'asdf':'321'
                    },
             },
    },
    'b':'2',
}

print(dict_bijiao(dict1,dict2))