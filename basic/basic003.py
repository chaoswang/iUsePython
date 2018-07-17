#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-20 22:27:34
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

def func1(x):
	def func2(y):
		return x * y
	return func2

print(func1(3)(7))
