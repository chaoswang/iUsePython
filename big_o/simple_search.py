#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-11 17:22:22
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

def simple_search(list, item):
	for guess in list:
		if guess == item:
			return list.index(guess)

my_list = [1, 3, 4, 7, 9]
print simple_search(my_list, 1)
print simple_search(my_list, 9)