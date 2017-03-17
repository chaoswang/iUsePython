#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Singleton():
    def __new__(cls, *more):
        if not hasattr(cls, '_inst'):
            #类似于java中的Singleton.class.newInstance()
            cls._inst = super(Singleton, cls).__new__(cls)
        return cls._inst


class SingleFruit(Singleton):
    #__new__()才是python中真正的构造函数，__init__()只是用来初始化属性的
    #__init__()有一个参数self，该self参数就是__new__()返回的实例
    def __init__(self, s):
        self.s = s


def main():
    apple = SingleFruit("apple")
    # 第二次调用构造函数时，实例不会重新创建，但是属性会重设
    banana = SingleFruit("banana")
    print(id(apple), apple.s)
    print(id(banana), banana.s)


if __name__ == '__main__':
    main()
