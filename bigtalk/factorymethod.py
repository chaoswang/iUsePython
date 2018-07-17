#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class LeiFeng:
    def sweep(self):
        print("LeiFeng sweep")

class Student(LeiFeng):
    def sweep(self):
        print("Student sweep")

class Volenteer(LeiFeng):
    def sweep(self):
        print("Volenteer sweep")

class LeiFengFactory:
    def createLeiFeng(self):
        pass

class StudentFactory(LeiFengFactory):
    def createLeiFeng(self):
        return Student()

class VolenteerFactory(LeiFengFactory):
    def createLeiFeng(self):
        return Volenteer()

if __name__ == '__main__':
    leiFengFactory = StudentFactory()
    leiFengFactory.createLeiFeng().sweep()
    leiFengFactory = VolenteerFactory()
    leiFengFactory.createLeiFeng().sweep()