#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-30 20:23:18
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

import random as r

class Fish(object):
	"""docstring for  Fish"""
	def __init__(self):
		self.x = r.randint(0, 10)
		self.y = r.randint(0, 10)
		
	def move(self):
		self.x -= 1
		print('my position is: ', self.x, self.y)

class Goldfish(Fish):
	"""docstring for Goldfish"""
	pass
		
class Shark(Fish):
	"""docstring for Shark"""
	def __init__(self):
		super().__init__()
		self.hungry = True

	def eat(self):
		if self.hungry:
			print('eat eat eat')
			self.hungry = False
		else:
			print('sleep sleep sleep')

fish = Fish()
fish.move()
		
goldfish = Goldfish()
goldfish.move()
goldfish.move()

shark = Shark()
shark.eat()
shark.eat()
shark.move()
