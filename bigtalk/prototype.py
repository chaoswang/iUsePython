#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 简历类Resume提供的Clone()方法其实并不是真正的clone，只是为已存在对象增加了一次引用。
# Python为对象提供的copy模块中的copy方法和deepcopy方法已经实现了原型模式，但由于例子的层次较浅，二者看不出区别。
import copy

class WorkExperience:
    def __init__(self, _place, _year):
        self.place = _place
        self.year = _year

    def __repr__(self):
        return self.place + ", " + str(self.year)

class Resume:
    def __init__(self, _name):
        self.name = _name

    def setAge(self, _age):
        self.age = _age

    def setWorkExperience(self, _we):
        self.we = _we

    def display(self):
        print(self.name + ", " + str(self.age) + ", " + str(self.we))

    def clone(self):
        return self

if __name__ == '__main__':
    a = Resume("James")
    b = a.clone()
    c = copy.copy(a)
    d = copy.deepcopy(a)
    a.setAge(7)
    b.setAge(12)
    c.setAge(15)
    d.setAge(18)
    a.setWorkExperience(WorkExperience("PrimarySchool",1996))
    b.setWorkExperience(WorkExperience("MidSchool",2001))
    c.setWorkExperience(WorkExperience("HighSchool",2004))
    d.setWorkExperience(WorkExperience("University",2007))
    a.display()
    b.display()
    c.display()
    d.display()