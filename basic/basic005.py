#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 23:11:20
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

f = lambda x : 2 * x + 1
print(f(1))

g = lambda x, y : x + y
print(g(1, 2))

print(list(filter(None, [1, 0, True, False])))

print(list(filter(lambda x : x % 2, range(10))))

print(list(map(lambda x : x * 2, range(5))))