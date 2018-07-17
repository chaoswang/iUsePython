#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-20 22:15:49
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

def func1():
	print('calling func1')
	def func2():
		print('calling func2')
	func2()

func1()
# func2()
