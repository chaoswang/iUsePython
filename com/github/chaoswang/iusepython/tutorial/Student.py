class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


zhang = Student("Zhang Shan", 100)
li = Student("Li Si", 90)
print(zhang.print_score())
print(li.print_score())
