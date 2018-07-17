#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-23 20:52:29
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

favoriate = 'fishC'
for i in favoriate:
	print(i, end=' ')

members = ['张三','李四','王五','赵六','孙七']
for each in members:
	print(each, len(each))


for x in range(1,10,2):
	print(x)

members.extend(['tom','jerry'])
members.insert(0,'mickey')
print(members)

tmp = members[0]
members[0] = members[1]
members[1] = tmp
print(members)

members.remove('mickey')
print(members)

del members[0]
print(members)

members.pop(1)
print(members)

print(members[:3])
print(members)