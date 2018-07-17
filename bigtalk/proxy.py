#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 为对象提供一种代理以控制对这个对象的访问。
class Interface:
    def request(self):
        pass

class RealSubject(Interface):
    def request(self):
        print("real request")

class proxy(Interface):
    def request(self):
        real = RealSubject()
        real.request()

def main():
    p = proxy()
    p.request()

if __name__ == '__main__':
    main()