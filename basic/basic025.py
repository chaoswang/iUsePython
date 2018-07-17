#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-11 23:22:59
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
	"""docstring for TSServProtocol"""
	def connectionMade(self):
		clnt = self.clnt = self.transport.getPeer().host
		print('...connected from', clnt)

	def dataReceived(self, data):
		self.transport.write(('[%s] %s' % (ctime(), data)).encode())

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()

