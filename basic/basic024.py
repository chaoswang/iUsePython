#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-07 20:37:46
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$
'''
BIF之描述符类
'''
class Celsius(object):
	"""docstring for Celsius"""
	def __init__(self, value = 26.0):
		self.value = float(value)

	def __get__(self, instance, owner):
		return self.value

	def __set__(self, instance, value):
		self.value = float(value)
		
class Fahrenheit(object):
	"""docstring for Fahrenheit"""
	def __get__(self, instance, owner):
		return instance.cel * 1.8 + 32

	def __set__(self, instance, value):
		instance.cel = (float(value) - 32) / 1.8
		
class Temperature(object):
	cel = Celsius()
	fah = Fahrenheit()
		
temp = Temperature()
print(temp.cel)
temp.cel = 30
print(temp.fah)
