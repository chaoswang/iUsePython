#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-14 20:28:24
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

def myGen():
	print('生成器被执行')
	yield 1
	yield 2

mg = myGen()
print(next(mg))
print(next(mg))

for each in myGen():
	print(each)

def fib():
	a = 0
	b = 1
	while True:
		a, b = b, a + b
		yield a

for each in fib():
	if each > 100:
		break
	print(each, end=' ')

#列表推导式，返回100以内能被3整除，但不能被2整除的数
a = [i for i in range(100) if not(i % 2) and i % 3]
print(a)
#字典推导式
b = {i : i % 2 == 0 for i in range(10)}
print(b)
#集合推导式，去除重复元素
c = {i for i in [1, 1, 2, 3, 3, 4, 5, 6, 6]}
print(c)

#生成器推导式
d = (i for i in range(100) if i % 2)
print(d)
print(next(d))
print(next(d))

print(sum(i for i in range(100) if i % 2))



