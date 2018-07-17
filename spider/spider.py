#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-28 19:52:46
# @Author  : chaoswang (263050006@qq.com)
# @Link    : https://github.com/chaoswang/
# @Version : $Id$

import urllib, urllib2

def getNovelListUrl():
	html = urllib.urlopen('http://www.quanshuwang.com/list/1_1.html').read()
	print html.decode('gbk').encode('utf-8')

getNovelListUrl()

