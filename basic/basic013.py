#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-27 21:39:20
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

def factorial(n):
	'''return n!'''
	return 1 if n < 2 else n * factorial(n - 1)

print(type(factorial))
print(factorial(5))

fact = factorial
print(list(map(fact, range(10))))