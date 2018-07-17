#! python3
# encoding=utf-8
# @Time    : 2017/12/10 13:03
# @Author  : chaoswang
# @File    : HelpTest.py

import com.github.chaoswang.soccer.tutorial.StringTest

com.github.chaoswang.soccer.tutorial.StringTest.printname('xx')

var = 300
print(com.github.chaoswang.soccer.tutorial.StringTest.changeme(var))
print(var)


com.github.chaoswang.soccer.tutorial.StringTest.arglist(1,2,3,4,5,6,6,7,8)

com.github.chaoswang.soccer.tutorial.StringTest.argdict(x=12,y=13,z=14)

def kwarg(**kwargs):
    print(str(kwargs))

kwarg(a=1,b=2)