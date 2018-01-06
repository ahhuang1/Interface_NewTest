#！/usr/bin/env.python
#coding:utf-8
import unittest
from public import base
#from public import HttpService


testcasefile = 'get_params_headers_test_data.xlsx'
AllData = base.get_data(testcasefile,'AllData')
TestData = base.get_data(testcasefile,'TestData')
EndPoint = AllData[1][1]
RequestMethod = AllData[1][2]
DataAll = TestData[1][1]
Expectedresult = TestData[1][2]
print(Expectedresult)
print(type(Expectedresult))

class GetParamsHeadersTest(unittest.TestCase):
    #get 有params和headers测试
    def setUp(self):
        #endpoint = 'get'
        #self.url = base.get_url(endpoint)
        self.url = base.get_url(EndPoint)

    def test_params_headers(self):
        #验证浏览器是否chrome
        # params={'show_env':1}
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        #     "Accept-Encoding": "gzip, deflate, sdch, br",
        #     'Accept':'*/*',
        #     'Connection':'keep-alive'
        # }
        #给服务器发送请求
        # DataALL = {'params':params,'headers':headers}
        DataALL = eval(DataAll)#从excel中取出的是字符串，需要用eval函数转换成字典
        #Method = 'get'  # 请求类型
        Method = RequestMethod
        # resp = HttpService.MyHTTP().get(self.url, **DataALL)
        resp = base.get_response(self.url, Method, **DataALL)
        print(resp)
        User_Agent = resp['headers']['User-Agent']
        self.assertIn(Expectedresult,User_Agent)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()