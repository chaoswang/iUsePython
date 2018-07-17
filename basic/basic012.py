#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-24 21:44:13
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

try:
	int('abc')
except Exception as e:
	print('出错啦：' + str(e))
else:
	print('没有任何异常')
finally:
	print('结束')


try:
	f = open('data.txt', 'w')
	for each_line in f:
		print(each_line)
except OSError as e:
	print('出错啦：' + str(e))
finally:
	f.close()

# 用with后不需要处理文件关闭，程序会自动关闭资源
try:
	with open('data.txt', 'w') as f:
		for each_line in f:
			print(each_line)
except OSError as e:
	print('出错啦：' + str(e))
