#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-20 22:08:34
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

count = 5
def myfunc():
	global count
	count = 10
	print(count)

myfunc()
print(count)
