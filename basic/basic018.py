#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-31 22:47:47
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

class CapsStr(str):
	"""构造"""
	def __new__(cls, arg_str):
		arg_str = arg_str.upper()
		return str.__new__(cls, arg_str)

a = CapsStr('I love fishc.com')
print(a)		


class ClassName(object):
	"""析构"""
	def __init__(self):
		print('我是__init__方法，我被调用了')
	def __del__(self):
		print('我是__del__方法，所有对对象的引用都被删除后，我会被垃圾回收调用')

cn = ClassName()
a = cn
b = cn
del a
del cn
del b
