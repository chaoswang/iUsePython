count = 5


def myFun():
    global count
    count += count
    print(count)


myFun()
