#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-14 15:22:15
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

class CountList:
	"""统计列表中元素被访问的次数"""
	def __init__(self, *args):
		self.values = [x for x in args]
		self.count = {}.fromkeys(range(len(self.values)), 0)

	def __len__(self):
		return len(self.values)

	def __getitem__(self, key):
		self.count[key] += 1
		return self.values[key]

c1 = CountList(1, 3, 5, 7, 9)
c2 = CountList(2, 4, 6, 8, 10)
print(c1[1])
print(c2[1])
print(c1.count)
print(c1[1] + c2[1])
print(c1.count)