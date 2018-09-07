import unittest
from public import base,read_xlsx
from ddt import ddt,unpack,data
from public.write_xls import *
from public.base import md5_pwd
import json
from public.Config import login_url
import requests
import os
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# print(BASE_PATH)#获取根目录
# print(os.path.realpath(__file__)) #获取当前文件路径
# print(os.path.dirname(os.path.realpath(__file__)))  # 从当前文件路径中获取目录
# print(os.path.basename(os.path.realpath(__file__))) #获取文件名
EXCEL_PATH = os.path.join(BASE_PATH,'test_data','test_data.xls')
#print(EXCEL_PATH)
test = read_xlsx.ExcelUtil(EXCEL_PATH, 'test').next()
newtable,newdata = ExcelUtil_write(EXCEL_PATH).new_tabe(0)


# def myskip():
#     for i in range(len(test)):
#         yield (test[i]['Skip'])
# skip = (test[i]['Skip'] for i in range(len(test)))


@ddt
class InterfaceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = {'username': 'huafeng', 'password': md5_pwd('000000')}
        rep = requests.post(login_url,data=data)
        cls.cookies_session = rep.cookies.get_dict()


    # @data(*test)
    # def setUp(self):
    #     if self.data['Skip'] == "True":
    #         b = True
    #     else:
    #         b = False
    #     unittest.skipIf(b, "跳过")
    #     print(1)

    # @data(*test)
    # def setUp(self,data):
    #     data = {'username': 'huafeng', 'password': md5_pwd('000000')}
    #     if data['is_login'] == "True":
    #         rep = requests.post(login_url,data=data)
    #         cookies_session = rep.cookies.get_dict()
    #     else:
    #         cookies_session = {}
    #     print(cookies_session,22)


    @data(*test)
    def test_interface(self,data):
        '''接口测试'''
        url = base.get_url(data['endpoint'])
        #判断测试是否跳过
        print('idbegin'+ data['CaseId'] +'idend')
        print('smbegin'+ data['Describe'] + 'smend')
        if data['Skip'] == "True":
            self.skipTest("跳过测试")
        if data['Params']:
            DataALL = eval(data['Params'])
            if data['MD5'] == "True":
                if data['MD5_parame']:
                    if DataALL.get('data'):
                        DataALL['data'][data['MD5_parame']] = md5_pwd(DataALL['data'][data['MD5_parame']])
                        #print(DataALL['data'][data['MD5_parame']])
                    if DataALL.get('json'):
                        DataALL['json'][data['MD5_parame']] = md5_pwd(DataALL['json'][data['MD5_parame']])
                        #print(DataALL['json'][data['MD5_parame']])
                    if DataALL.get('params'):
                        DataALL['params'][data['MD5_parame']] = md5_pwd(DataALL['params'][data['MD5_parame']])
                        #print(DataALL['params'][data['MD5_parame']])
        else:
            DataALL = {}
        Method = data['RequestSend']
        if data['is_login'] == "True":
            cookies_session = InterfaceTest.cookies_session
        else:
            cookies_session = {}
        resp = base.get_response(url, Method,cookies_session, **DataALL)
        print(resp)

        #获取用例行，将响应结果写入表格中
        CaseId = data['CaseId']
        #print(CaseId)
        row = base.get_row(test,CaseId)
        #print(row)
        newtable.write(row, 7, str(resp))

        Expectedresult = eval(data['ExpectResult'])
        self.a=base.dict_bijiao(Expectedresult,resp)
        self.assertEqual(self.a,True)


    @classmethod
    def tearDownClass(cls):
        newdata.save(EXCEL_PATH)

if __name__ == '__main__':
    unittest.main()