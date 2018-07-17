# coding:utf8

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    # 这是Python函数可变参数 args及kwargs,*args表示任何多个无名参数，它是一个tuple,**kwargs表示关键字参数，它是一个dict
    def __call__(self, *args, **kwargs):
        print('My name is %s...' % self.name)
        print('My friend is %s...'  % args)
        print('My boss is %s...'  % kwargs)

p = Person('Bob', 'male')
tuple1 = ('Tim', 'Tom')
p(tuple1)
# 问什么下面这样的调用不成功？？？？
# dict1 = {'Adam':100}
# p(dict1)


# def foo(*args,**kwargs):
#     print('args=',args)
#     print('kwargs=',kwargs)
#     print('**********************')
#
# if __name__=='__main__':
#     foo(1,2,3)
#     foo(a=1,b=2,c=3)
#     foo(1,2,3,a=1,b=2,c=3)
#     foo(1,'b','c',a=1,b='b',c='c')
