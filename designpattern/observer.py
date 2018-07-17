#!/usr/bin/env python3
# coding:utf-8
'''
定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时, 所有依赖于它的对象都得到通知并被自动更新。
'''

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self.observers:
            observer.update(self)

# Example usage
class Data(Subject):
    def __init__(self, name=""):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    # 把属性隐藏，外部要获取该属性只能通过该方法来调用，Python内置的@property装饰器就是负责把一个方法变成属性调用的
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

# observers
class HexViewer:
    def update(self, subject):
        print("HexViewer: Subject %s has data 0x%x" %(subject.name, subject.data))

class DecimalViewer:
    def update(self, subject):
        print("DecimalViewer: Subject %s has data %d" %(subject.name, subject.data))

if __name__ == '__main__':
    data1 = Data("Data 1")
    data2 = Data("Data 2")
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view1)
    data2.attach(view2)

    print("Setting Data1 = 10")
    data1.data = 10# 实际转化为data1.set_data(60)
    print("Setting Data2 = 15")
    data2.data = 15
    print("Setting Data1 = 3")
    data1.data = 3
    print("Setting Data2 = 5")
    data2.data = 5
    print("Detach HexViewer from data1 and data2.")
    data1.detach(view2)
    data2.detach(view2)
    print("Setting Data 1 = 10")
    data1.data = 10
    print("Setting Data 2 = 15")
    data2.data = 15