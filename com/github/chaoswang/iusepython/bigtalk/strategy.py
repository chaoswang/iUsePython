#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Cashier :
    def cash(self, money):
        pass

class CashNormal(Cashier):
    def cash(self, money):
        return money

class CashRebate(Cashier):
    def __init__(self, _discount):
        self.discount = _discount

    def cash(self, money):
        return money * self.discount

class CashReturn(Cashier):
    def __init__(self, _total, _ret):
        self.total = _total
        self.ret = _ret

    def cash(self, money):
        if money >= self.total:
            return money - self.ret
        else:
            return money

class CashContext:
    def __init__(self, cashier):
        self.context = cashier

    def getPayment(self, money):
        print(self.context.cash(money))

if __name__ == '__main__':
    money = input("money:")
    type = input("promote type::[1]for normal,[2]for 80% discount [3]for 300 -100.")
    strategy = {"1":CashNormal(), "2":CashRebate(0.8), "3":CashReturn(300, 100)}
    if type in ["1","2","3"]:
        cc = CashContext(strategy[type])
    else:
        print("Undefine type.Use normal mode.")
        cc = CashContext(strategy[1])
    cc.getPayment(int(money))