# 描述一个程序员的工作状态，当需要改变状态时发生改变，不同状态下的方法实现不同
class State:
    def write_program(self):
        pass

class NoonState(State):
    def write_program(self, w):
        print("noon working")
        if(w.hour < 13):
            print("fun.")
        else:
            print("need to rest.")

class ForenoonState(State):
    def write_program(self, w):
        if(w.hour < 12):
            print("morning working")
            print("energetic")
        else:
            w.set_state(NoonState())
            w.write_program()

class Work:
    def __init__(self):
        self.hour = 9
        self.current_state = ForenoonState()

    def set_state(self, _state):
        self.current_state = _state

    def write_program(self):
        self.current_state.write_program(self)

def main():
    mywork = Work()
    mywork.hour = 9
    mywork.write_program()
    mywork.hour = 12
    mywork.write_program()

if __name__ == '__main__':
    main()


