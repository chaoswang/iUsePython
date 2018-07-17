#coding:utf8

def count_to(count):
    numbers = ["one", "two", "three", "four", "five"]
    for pos, number in zip(range(count), numbers):
        yield number

count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)

print('Counting to two...')
for number in count_to_two():
    print(number)

print('Counting to five...')
for number in count_to_five():
    print(number)

# #二维矩阵变换（矩阵的行列互换）
# x = [1, 2, 3]
# y = [4, 5, 6]
# z = [7, 8, 9]
# xyz = zip(x, y, z)
# for i in xyz:
#     print(i)

# x = range(5)
# y = ["one", "two", "three", "four", "five"]
# xy = zip(x, y)
# for i in xy:
#     print(i)

# #生成器
# mylist = [x*x for x in range(3)]
# print(mylist)
# mygenerator=(x*x for x in range(3))
# for i in mygenerator:
#     print (i)

# # 生成器生成斐波那契数列
# def fib(max):
#     a, b = 1, 1
#     while a < max:
#         yield a
#         a, b = b, a+b
#
# for n in fib(15):
#     print(n)
#
# m = fib(13)
# print(m)
# print(m.next())
# print(m.next())
# print(m.next())