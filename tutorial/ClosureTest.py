# 闭包
def count():
    i = 2

    def f(j):
        return j ** i

    # 把内部函数作为返回值返回
    return f


f1 = count()
print(f1.__closure__)
print(f1(2))


# 非闭包
def count():
    i = 2

    def f(j, i=i):
        return j ** i

    # 把内部函数作为返回值返回
    return f


f1 = count()
print(f1.__closure__)
print(f1(2))

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
