# 展示一个人一件一件穿衣服的过程
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("dressed %s" %(self.name))

class Clothes:
    def decorate(self, showable):
        self.showable = showable

    def show(self):
        self.showable.show()

class Underwear(Clothes):
    def show(self):
        print("wear Underwear")
        self.showable.show()

class Trouser(Clothes):
    def show(self):
        print("wear Trouser")
        self.showable.show()

def main():
    p = Person("somebody")
    underwear = Underwear()
    underwear.decorate(p)
    trouser = Trouser()
    trouser.decorate(underwear)
    trouser.show()

if __name__ == '__main__':
    main()