#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-24 17:59:12
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

tuple1 = ('tom', 'jerry', 'mickey', 'minnie')
tuple2 = tuple1[:2] + ('bluto',) + tuple1[2:]
print(tuple2)

del tuple1
print(tuple1)