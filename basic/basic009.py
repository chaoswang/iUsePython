#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-24 16:56:08
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

list1 = [123, 456]
list2 = [234, 567]
print(list1 < list2)

list3 = list1 + list2
print(list3)

list4 = list1 * 2
print(list4)
print(list4.count(456))

print(999 not in list4)

list5 = [4,3,6,5,9,1,2,0,8]
list5.sort()
print(list5)
list5.reverse()
print(list5)
list5.sort(reverse=False)
print(list5)