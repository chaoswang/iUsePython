#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-14 15:59:25
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

string = 'fishc'
for each in string:
	print(each)

it = iter(string)#bif:__iter__()
while True:
	try:
		each = next(it)#bif:__next__()
	except StopIteration:
		break
	print(each)


class Fibs(object):
	"""用迭代器实现斐波那契数列"""
	def __init__(self, n=20):
		self.a = 0
		self.b = 1
		self.n = n

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > self.n:
			raise StopIteration
		return self.a
		
fibs = Fibs(100)
for each in fibs:
	print(each)