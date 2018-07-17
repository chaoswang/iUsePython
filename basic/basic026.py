#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-11 23:32:36
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567

class TSClntProtocol(protocol.Protocol):
	def sendData(self):
		data = input('> ')
		if data:
			print('...sending %s...' % data)
			self.transport.write(data.encode())
		else:
			self.transport.loseConnection()

	def connectionMade(self):
		self.sendData()

	def dataReceived(self, data):
		print(data.decode())
		self.sendData()

class TSClntFactory(protocol.ClientFactory):
	protocol = TSClntProtocol
	clientConnectionLost = clientConnectionFailed = lambda self, connector, reason : reactor.stop()
		
reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
