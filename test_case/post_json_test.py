#！/usr/bin/env.python
#coding:utf-8

from public import base
#from public import HttpService
import unittest

testcasefile = 'post_json_test_data.xlsx'
AllData = base.get_data(testcasefile,'AllData')
TestData = base.get_data(testcasefile,'TestData')
EndPoint = AllData[1][1]
RequestMethod = AllData[1][2]
Sn = TestData[1][0]
RequestData = TestData[1][1]
Expectedresult = TestData[1][2]

class PostJsonTest(unittest.TestCase):
    def setUp(self):
        # endpoint = 'post'
        # self.url = base.get_url(endpoint)
        self.url = base.get_url(EndPoint)
    def test_post_json(self):

        # params={'show_env':1}
        # json={"info":{"code":1,"sex":"男","id":1900,"name":"黄爱华"},
        # "code":1,
        # "name":"huangaihau黄爱华huangaihau黄爱华黄爱华 ","sex":"女",
        # "data":[{"code":1,"sex":"男","id":1900,"name":"黄爱华"},{"code":1,"sex":"女","id":1900,"name":"黄爱华"}],
        # "id":1900
        # }
        # DataALL = {'params':params,'json':json}
        # resp = HttpService.MyHTTP().post(self.url,**DataALL)
        # Method = 'post'  # 请求类型
        DataALL = eval(RequestData)
        Method = RequestMethod
        resp = base.get_response(self.url, Method, **DataALL)
        print(resp)
        name = resp.get('data')

        print(name)
        self.assertIsInstance(Expectedresult,str)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
