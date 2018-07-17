#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-19 19:06:50
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

import threading
from time import sleep, ctime

loops = [4,2]

def loop(nloop, nsec):
	print('start loop', nloop, 'at: ', ctime())
	sleep(nsec)
	print('stop loop', nloop, 'at: ', ctime())
	
def main():
	print('starting at:', ctime())
	threads = []
	nloops = range(len(loops))
	for i in nloops:
		t = threading.Thread(target = loop, args = (i, loops[i]))  #分配locktype锁对象
		threads.append(t)  
	for i in nloops:
		threads[i].start()
	for i in nloops:
		threads[i].join()  #等待所有线程结束
	print('stopping at:', ctime())

if __name__ == '__main__':
	main()