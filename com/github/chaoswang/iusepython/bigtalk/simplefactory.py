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



