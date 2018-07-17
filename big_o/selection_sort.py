#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-11 20:06:21
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

def find_smallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selection_sort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = find_smallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

print selection_sort([5,7,3,9,2])