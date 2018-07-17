#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-11 17:29:39
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

def binary_search(list, item):
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = (low + high) / 2
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

my_list = [1, 3, 4, 7, 9]
print binary_search(my_list, 1)
print binary_search(my_list, 9)