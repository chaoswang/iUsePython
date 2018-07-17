#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-18 22:19:52
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

import _thread #模块前面加下划线，可能表示该模块已经deprecated了，被threading模块代替
from time import sleep, ctime

loops = [4,2]

def loop(nloop, nsec, lock):
	print('start loop', nloop, 'at: ', ctime())
	sleep(nsec)
	print('stop loop', nloop, 'at: ', ctime())
	lock.release()  #释放锁

def main():
	print('starting at:', ctime())
	locks = []
	nloops = range(len(loops))
	for i in nloops:
		lock = _thread.allocate_lock()  #分配locktype锁对象
		lock.acquire()  #尝试获取锁对象
		locks.append(lock)  
	for i in nloops:
		_thread.start_new_thread(loop, (i, loops[i], locks[i]))
	for i in nloops:
		while locks[i].locked(): pass  #如果获取到了锁对象则返回ture
	print('stopping at:', ctime())

if __name__ == '__main__':
	main()