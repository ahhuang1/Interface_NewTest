#！/usr/bin/env.python
#coding:utf-8

import unittest
from unittest import mock




class Foo1():
    def add1(self,a,b):
        return a + b
    def add2(self,a,b):
        return a + b + 1

class Foo2():
    def add1(self,a,b):
        return a + b + 2
    def add2(self,a,b):
        return a + b + 3

class Foo3():
    def add1(self,a,b):
        return  a + b + 4

mockFoo1 = mock.Mock(spec = Foo1,return_value=Foo2())
print(mockFoo1)
mockFoo2 = mock.Mock(spec = Foo2,return_value=Foo3())
print(mockFoo2)
print(mockFoo1().add1(2,3))
print(mockFoo2().add1(2,3))

mockFoo1.attach_mock(mockFoo2,'foorBar')
print(mockFoo1.foorBar().add1(2,3))

mockFoo3 = mock.Mock(spec = Foo3)

mockFoo3.mock_add_spec(Foo1)
print(mockFoo3.add2(2,3))