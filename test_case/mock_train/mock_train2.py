#！/usr/bin/env.python
#coding:utf-8

import sys
import unittest
from unittest import mock
sys.path.append('./mock_train')
from test_case.mock_train import modular


'''1.mock一个对象'''
class TestCount1(unittest.TestCase):
    @mock.patch('modular.add_def')#1
    def test_add(self,mock_add_def):#2
        mock_add_def.return_value=1#3
        mock_add_def.side_effect = modular.add_def2
        result = modular.add_def(8,5)
        print(result)
        self.assertEqual(result,13)

'''2.mock对象里的一个方法'''
class TestCount2(unittest.TestCase):
    @mock.patch.object(modular.Count,'add') #1 @mock.patch.object
    def test_add(self,mock_add):#2
        count = modular.Count()
        mock_add.return_value = 2 #3
        mock_add.side_effect = modular.add_def2
        result = count.add(8,5)
        print(result)
        self.assertEqual(result,13)

'''3.mock多个函数，注意顺序'''
class TestCount3(unittest.TestCase):

    @mock.patch.object(modular.Count, 'add')  # 1 @mock.patch.object
    @mock.patch('modular.add_def')#1 @mock.patch
    def test_add(self,mock_add_def,mock_add):#参数的顺序与装饰的顺序是反的，与self是相同的
        count = modular.Count()
        mock_add_def.return_value = 1 #3
        mock_add.return_value = 2 #3
        result1 = count.add(8,5)
        result2 = modular.add_def(8,5)
        print(result1,result2)
        self.assertEqual(result1,13)
        self.assertEqual(result2,13)

    if __name__ == '__main__':
        unittest.main()