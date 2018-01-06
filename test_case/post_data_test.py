#！/usr/bin/env.python
#coding:utf-8
#第一步导入模块
import unittest
from public import base
#from public import HttpService

#第二步：必须继承unittest.TestCase
class PostDataTest(unittest.TestCase):
    #Post, data测试
    #第三步：主要配置环境，进行测试前的初始化工作，比如在接口测试前面做一些前置的参数赋值，数据库操作等

    def setUp(self):
        endpoint = 'post'
        self.url = base.get_url(endpoint)

    #第4步：定义测试用例，名字以‘test’开头
    def test_post_data_1(self):
        #form值验证
        params = {'show_env': 1}
        data = {'a': '黄爱华', 'b': 'form-data'}
        DataALL = {'params':params,'data':data}
        # resp = HttpService.MyHTTP().post(self.url,**DataALL)
        Method = 'post'  # 请求类型
        resp = base.get_response(self.url, Method, **DataALL)
    #第五步：定义assert断言，判断测试结果
        form = resp['form']['a']
        #form = resp.get('form').get('a')
        try:
            self.assertEqual(form,'黄爱华')
            print('通过')
        except:
            print('失败')


    @unittest.skip('无条件跳过')
    def test_post_data_2(self):
        #form值验证
        params = {'show_env': 1}
        data = {'a': '黄爱华', 'b': 'form-data'}
        DataALL = {'params':params,'data':data}
        #resp = HttpService.MyHTTP().post(self.url,**DataALL)
        Method = 'post'  # 请求类型
        resp = base.get_response(self.url, Method, **DataALL)
    #第五步：定义assert断言，判断测试结果
        #form = resp['form']['a']
        form = resp.get('form').get('a')
        self.assertEqual('黄爱华',form)
        self.assertIsInstance(form,str)

    #第六步：清理环境：测试后的测试工作，比如参数还原或销毁，数据库的还原恢复等
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
