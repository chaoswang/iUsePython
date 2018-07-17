#! python3
#encoding=utf-8

var = ['hello', '''hello''',"""hello""", '''hello "dear"''']
print(var)

s = "my name is %s and age is %d" % ('wc',31)

def printname(str):
    "print name"
    print(str)

def changeme(var):
    var = 100
    return var

def arglist(a, *b):
    print(a)
    print(b)

def argdict(**a):
    print(a)