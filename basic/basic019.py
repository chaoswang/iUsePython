#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-04 22:11:45
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

from socket import *
from time import ctime

HOST = '' 
BUFSIZ = 1024
TCP_ADDR = (HOST, 21567)
UDP_ADDR = (HOST, 21568)

# TCP服务器
# tcpSerSock = socket(AF_INET, SOCK_STREAM)
# tcpSerSock.bind(TCP_ADDR)
# tcpSerSock.listen(5)

# while True:
# 	print('wating for connection...')
# 	tcpCliSock, addr = tcpSerSock.accept()
# 	print('...connected from: ', addr)

# 	while True:
# 		data = tcpCliSock.recv(BUFSIZ).decode()
# 		if not data:
# 			break
# 		tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode())
# 	tcpCliSock.close()
# tcpSerSock.close()

# UDP服务器
udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(UDP_ADDR)

while True:
	print('wating for message...')
	data, addr = udpSerSock.recvfrom(BUFSIZ)
	udpSerSock.sendto(('[%s] %s' % (ctime(), data)).encode(), addr)
	print('...recvfrom and sendto:', addr)

udpSerSock.close()





















