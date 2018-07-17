#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-04 23:08:32
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

from socket import *

HOST = 'localhost' 
BUFSIZ = 1024
TCP_ADDR = (HOST, 21567)
UDP_ADDR = (HOST, 21568)

# TCP客户端
# tcpCliSock = socket(AF_INET, SOCK_STREAM)
# tcpCliSock.connect(ADDR)

# while True:
# 	data = input('> ')
# 	if not data:
# 		break
# 	tcpCliSock.send(data.encode())
# 	data = tcpCliSock.recv(BUFSIZ)
# 	if not data:
# 		break
# 	print(data.decode())
# tcpCliSock.close()

# UDP客户端
udpCliSock = socket(AF_INET, SOCK_DGRAM)
while True:
	data = input('> ')
	if not data:
		break
	udpCliSock.sendto(data.encode(), UDP_ADDR)
	data, UDP_ADDR = udpCliSock.recvfrom(BUFSIZ)
	if not data:
		break
	print(data.decode())
udpCliSock.close()
