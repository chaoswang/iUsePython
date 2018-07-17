#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-19 22:41:46
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

import re

secret_code = 'sfaerdsafxxIxx;lsjf23435xxlovexx23wefsndvxxyouxxosnvoh2983us'

b = re.search('xx(.*?)xx', secret_code).group(1)
print(b)
