# 四则运算计算器，根据用户的输入产生相应的运算类，用这个运算类处理具体的运算。
class Operation:
    def do_operation(self, a, b):
        pass

class OperationAdd(Operation):
    def do_operation(self, a, b):
        return a+b

class OperationMinus(Operation):
    def do_operation(self, a, b):
        return a-b

class OperationMultiply(Operation):
    def do_operation(self, a, b):
        return a*b

class OperationDivide(Operation):
    def do_operation(self, a, b):
        return a/b

def get_operation_from_factory(operation_str):
    factory = {"+":OperationAdd,"-":OperationMinus,"*":OperationMultiply,"/":OperationDivide}
    return factory[operation_str]

def main():
    op = input("operator: ")
    a = input("a: ")
    b = input("b: ")
    operation = get_operation_from_factory(op)()
    print(operation.do_operation(int(a),int(b)))

if __name__ == '__main__':
    main()



