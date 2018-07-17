#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-23 20:07:10
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

def avg(first, *rest):
	return (first + sum(rest))/(1 + len(rest))

print(avg(3,4,5,6))
