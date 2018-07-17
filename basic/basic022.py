#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-07 14:08:49
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

class AttrTest(object):
	"""docstring for AttrTest"""
	def __getattribute__(self, name):
		print('__getattribute__')
		return super.__getattribute__(name)

	#获取不到指定属性时，会调用该方法
	def __getattr__(self, name):
		print('__getattr__')

	def __setattr__(self, name, value):
		print('__setattr__')
		super.__setattr__(name, value)

	def __delattr__(self, name):
		print('__delattr__')
		super.__delattr__(name, value)

class Rectangle(object):
	"""docstring for Rectangle"""
	def __init__(self, width=0, height=0):
		self.width = width
		self.height = height

	def __setattr__(self, name, value):
		if name == 'square':
			self.width = value
			self.height = value
		else:
			# super().__setattr__(name, value)  #推荐调用基类的方法 
			self.__dict__[name] = value

	def getarea(self):
		return self.width * self.height

r = Rectangle()
r.square = 3
print(r.getarea())

r = Rectangle(4, 5)
print(r.getarea())