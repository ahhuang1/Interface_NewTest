#！/usr/bin/env.python
#coding:utf-8

import unittest
from public import base
#from public import HttpService
import unittest
from public import base
from unittest import mock
import requests
from mock_data.get_params_test_mock import *



class GetParams(unittest.TestCase):
    '''GetParams测试'''
    def setUp(self):
        endpoint = 'get'
        self.url = base.get_url(endpoint)

    def test_get_params(self):
        '''test_get_params1测试'''
        params = {'show_env':1}
        '''
        给服务器发送请求
        '''
        DataALL = {'params': params}
        Method = 'get'  # 请求类型
        # resp = HttpService.MyHTTP().get(self.url, **DataALL)
        resp = base.get_response(self.url, Method, **DataALL)

        if base.get_mock_status() == 'ON':
            mockresp = mock.Mock(side_effect=mockFoo)
            resp = mockresp('success')
            #mockresp.assert_called_with()
            print(mockresp.called)
            mockresp.reset_mock()

        connect = resp.get('headers').get('Connection')
        self.assertEqual(connect,'close')

    def test_get_params2(self):
        '''test_get_params2测试'''
        params = {'show_env': 1}
        '''
        给服务器发送请求
        '''
        DataALL = {'params': params}
        Method = 'get'#请求类型
        #resp = HttpService.MyHTTP().get(self.url, **DataALL)
        resp = base.get_response(self.url,Method,**DataALL)


        connect = resp.get('headers').get('Connection')
        self.assertIsInstance(connect, str)

    def test_get_params3(self):
        '''test_get_params3测试'''
        params = {'show_env':1}
        resp = requests.get(self.url,params=params)

        if base.get_mock_status() == 'ON':
            mockresp = mock.Mock(side_effect=mockFoo)
            resp.status_code = mockresp('success').get('status_code')
            print(resp)
            mockresp.reset_mock()

        result = resp.status_code
        self.assertEqual(result,200)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
