#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-24 21:21:38
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

def showMaxFactor(num):
	count = num // 2
	while count > 1:
		if num % count == 0:
			print('%d 的最大约数是 %d' % (num, count))
			break
		count -= 1
	else:
		print('%d 是素数' % num)

num = int(input('请输入数字: '))
showMaxFactor(num)