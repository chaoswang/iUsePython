#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-31 22:34:30
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

class PropertyTest(object):
	"""docstring for PropertyTest"""
	def __init__(self, size):
		self.size = size

	def get_size(self):
		return self.size

	def set_size(self, value):
		self.size = value
	
	def del_size(self):
		del self.size

	x = property(get_size, set_size, del_size)

pt = PropertyTest(1)
print(pt.x)
pt.x = 2
print(pt.x)
del pt.x
print(pt.x)