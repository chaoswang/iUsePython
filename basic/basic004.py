#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-20 22:31:41
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

def func1():
	x = 5
	def func2():
		nonlocal x
		x *= x
		return x 
	return func2()

print(func1())