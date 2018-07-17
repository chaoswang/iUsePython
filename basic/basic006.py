#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 23:36:29
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

def myfunc(x):
	i = j = 1
	while i <= x:
	 	j = i * j
	 	i += 1
	return j		
print(myfunc(5))


def factorial(n):
	result = n
	for i in range(1,n):
		result *= i
	return result
print(factorial(5))


def recursion(n):
	if n == 1:
		return 1
	else:
		return n * recursion(n-1)
print(recursion(5))

