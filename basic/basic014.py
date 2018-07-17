#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-27 21:55:18
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

import random
secret = random.randint(1, 10)
print(secret)

import os
print(os.getcwd())
os.chdir('E:\\workspace_py\\python100')
print(os.listdir(os.getcwd()))

print(os.path.basename('E:\\workspace_py\\python100\\basic\\basic001.py'))


import time
print(time.gmtime(os.path.getatime('E:\\workspace_py\\python100\\basic\\basic001.py')))
