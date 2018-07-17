#!/usr/bin/env python3
# coding:utf-8

# 在软件系统中，行为请求者与行为实现者通常是一种紧耦合的关系
# 在某些场合，比如要对行为进行"记录、撤销/重做、事务"等处理，这种无法抵御变化的紧耦合是不合适的。
# 在这种情况下，如何将"行为请求者"与"行为实现者"解耦？将一组行为抽象为对象，可以实现二者之间的松耦合。

class Chef:
    def cookChicken(self):
        print('Chicken done!')

    def cookVegetable(self):
        print('Vegetable done!')

class Command:
    def __init__(self, chef):
        self.chef = chef

    def execute(self):
        pass

class CookChickenCmd(Command):
    def execute(self):
        self.chef.cookChicken()

class CookVegetableCmd(Command):
    def execute(self):
        self.chef.cookVegetable()

class Waiter:
    def __init__(self):
        self.order = []

    # 根据客人的点单情况，记录点菜单
    def addCmd(self, *cmd):
        for c in cmd:
            self.order.append(c)

    def notifyChef(self):
        for cmd in self.order:
            cmd.execute()

if __name__ == '__main__':
    chef = Chef()
    waiter = Waiter()
    waiter.addCmd(CookChickenCmd(chef), CookVegetableCmd(chef))
    waiter.notifyChef()


