#! python3
# encoding=utf-8
# @Time    : 2017/12/10 19:29
# @Author  : chaoswang
# @File    : Employee.py

class Employee:
    classstr = "field 1"
    def __init__(self, name , pay):
        self.name = name
        self.pay = pay

    def hello(self):
        print(self.name)
        print(self.pay)

def main():
    worker = Employee('tom', 11)
    print(hasattr(worker, 'classstr'))
    print(Employee.__module__)

if __name__ == '__main__':
    main()