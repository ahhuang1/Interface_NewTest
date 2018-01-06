#！/usr/bin/env.python
#coding:utf-8

import unittest
from unittest import mock
from .modular import Count


class TestCount(unittest.TestCase):

    def test_case(self):
        count = Count()
        count.add = mock.Mock(name='add',return_value=7)
        #count.add = mock.Mock(return_value=count.add(2,3))
        count.add = mock.Mock(return_value=7,side_effect=count.add2)
        count.add.configure_mock(return_value=8)
        count.add.configure_mock(side_effect=count.add3)
        print(count.add)
        result = count.add(8,5)
        count.add.assert_called_with(8,5)#检查最近一次的调用
        count.add.assert_called_once_with(8,5)#检查最近一次的调用，只能调用一次
        count.add(2,3)
        count.add.assert_called_with(2,3)
        count.add.assert_any_call(8,5)#检查是否曾经调用

        print(count.add.call_args_list)
        param1 = mock.call(8,5)
        param2 = mock.call(2,3)
        count.add.assert_has_calls([param1,param2],any_order= False)#检查方法调用的顺序，any_order为false时，检查顺序。默认为false
        count.add.assert_has_calls([param2,param1],any_order= True)

        print(result)
        print(count.add.called)#检查是否调用
        print(count.add.call_count)#检查调用的次数
        print(count.add.call_args)#检查最近调用的参数
        print(count.add.call_args_list)#只有参数调用(工厂)

        mockFoo = mock.Mock(spec=Count)
        mockFoo.add(1, 1)
        mockFoo.add(1, 2)
        print(mockFoo.method_calls)#只有方法调用
        print(mockFoo.mock_calls)#包含参数调用（工厂），以及方法


        self.assertEqual(result,16)

    if __name__ == '__main__':
        unittest.main()