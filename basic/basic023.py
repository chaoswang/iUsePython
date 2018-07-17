#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-07 15:43:54
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

class MyDescriptor(object):
	"""docstring for MyDescriptor"""
	def __get__(self, instance, owner):
		print('getting...', self, instance, owner)

	def __set__(self, instance, value):
		print('setting...', self, instance, value)

	def __delete__(self, instance):
		print('deleting...', self, instance)
		
class Test(object):
	"""docstring for Test"""
	x = MyDescriptor()
		
t = Test()
print(t.x)
t.x = 'x-man'
print(t.x)
del t.x
print(t.x)

class MyProperty(object):
	"""docstring for MyProperty"""
	def __init__(self, fget=None, fset=None, fdel=None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel

	def __get__(self, instance, owner):
		return self.fget(instance)

	def __set__(self, instance, value):
		return self.fset(instance, value)

	def __delete__(self, instance):
		return self.fdel(instance)

class C(object):
	"""docstring for C"""
	def __init__(self):
		self._x = None
		
	def getX(self):
		return self._x

	def setX(self, value):
		self._x = value

	def delX(self):
		del self._x
	x = MyProperty(getX, setX, delX)

c = C()
print(c.x)
c.x = 'x-man'
print(c._x)
# del c.x
print(c.x)