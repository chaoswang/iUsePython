#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-18 21:27:49
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

import _thread
from time import sleep, ctime

def loop0():
	print('start loop 0 at:', ctime())
	sleep(4)
	print('stop loop 0 at:', ctime())

def loop1():
	print('start loop 1 at:', ctime())
	sleep(2)
	print('stop loop 1 at:', ctime())

def main():
	print('starting at:', ctime())
	_thread.start_new_thread(loop0, ())
	_thread.start_new_thread(loop1, ())
	sleep(5)
	print('stopping at:', ctime())

if __name__ == '__main__':
	main()