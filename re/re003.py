#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-26 23:12:56
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

import re

print(re.search(r'fish(c|d)', 'fishd'))
print(re.search(r'^fish(c|d)', 'i love fishd'))
print(re.search(r'^fish(c|d)', 'fishd i love '))
print(re.search(r'(fishc)\1', ' i love fishcfishc'))