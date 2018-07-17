#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-07 11:15:51
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

import time as t

class MyTimer(object):
	"""docstring for MyTimer"""
	def __init__(self):
		self.unit = ['年', '月', '日', '时', '分', '秒']
		self.prompt = '未开始计时'
		self.lasted = []
		self.begin = 0
		self.end = 0

	def __str__(self):
		return self.prompt
	#__str__是面向用户的，str或print时会显示，而__repr__面向程序员的，打印变量会显示
	__repr__ = __str__ 

	def __add__(self, other):
		prompt = '总共运行了'
		result = []
		for i in range(6):
			result.append(self.lasted[i] + other.lasted[i])
			if self.lasted[i]:
				prompt += (str(result[i]) + self.unit[i])
		return prompt

	def start(self):
		self.begin = t.localtime()#属性名不要和方法名同名
		self.prompt = '请先调用stop停止计时'
		print('开始计时')

	def stop(self):
		if not self.start:
			print('请先调用start开始计时')
		else:
			self.end = t.localtime()
			self._calc()
			print('结束计时')
		
	def _calc(self):
		self.lasted = []
		self.prompt = '总共运行了'
		for i in range(6):
			self.lasted.append(self.end[i] - self.begin[i])
			if self.lasted[i]:
				self.prompt += (str(self.lasted[i]) + self.unit[i])
		#为下一轮计时初始化
		self.begin = 0
		self.end = 0


t1 = MyTimer()
print(t1)
t1.start()
t.sleep(1)
t1.stop()
print(t1)

t2 = MyTimer()
t2.start()
t.sleep(2)
t2.stop()
print(t2)
print(t1 + t2)