#！/usr/bin/env.python
#coding:utf-8

from public import base
import unittest
import requests
import json
from ddt import ddt,data,unpack

testcasefile = 'get_nothing_test_data.xlsx'
AllData = base.get_data(testcasefile,'AllData')
TestData = base.get_data(testcasefile,'TestData')[1:]
TestData1 = TestData[0][0:3]
TestData2 = TestData[1][0:3]
TestData = [TestData1,TestData2]
print(TestData)

@ddt
class GetNothingTest(unittest.TestCase):
    #get无参数测试
    def setUp(self):
        self.endpoint = AllData[1][1]
        self.RequestMethod = AllData[1][2]
        self.RequestData = AllData[1][3]
        #endpoint = 'get'
        self.url = base.get_url(self.endpoint)

    @data(200,400,500,201)
    def test_1(self,result):
        #检验状态码是否为200
        r = requests.get(self.url)

        status_code = r.status_code
        self.assertEqual(status_code,result)

    #@data(('headers','Connection','close'),('headers','Host','httpbin.org'))
    # @data(['headers', 'Connection', 'close'], ['headers', 'Host', 'httpbin.org'])
    @data(*TestData)
    @unpack
    def test_2(self,headers,key,result):
        #校验headers里的Connection值
        # r = requests.get(self.url)
        # resp = r.json()
        # connect = resp[headers][value]
        Method = self.RequestMethod
        resp = base.get_response(self.url,Method)
        connect = resp[headers][key]
        self.assertEqual(connect,result)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
