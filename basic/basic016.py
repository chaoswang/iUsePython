#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-30 20:43:34
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

class Turtle(object):
	"""docstring for Turtle"""
	def __init__(self, x):
		self.num = x
		
class Fish(object):
	"""docstring for Fish"""
	def __init__(self, x):
		self.num = x

class Pool(object):
	"""不使用继承，使用组合"""
	def __init__(self, x, y):
		self.turtle = Turtle(x)
		self.fish = Fish(y)
		
	def print_num(self):
		print('有 %d 只乌龟，有 %d 只鱼' % (self.turtle.num, self.fish.num))


pool = Pool(1, 2)
pool.print_num()