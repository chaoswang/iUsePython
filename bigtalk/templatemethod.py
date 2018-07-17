# 考试时使用同一种考卷（父类），不同学生上交自己填写的试卷（子类方法的实现）
class TestPaper:
    def question1(self):
        print("Q1 option: A; B; C; D;")
        print("(%s)" %self.answer1())

    def question2(self):
        print("Q2 option: A; B; C; D;")
        print("(%s)" %self.answer2())

    def answer1(self):
        pass

    def answer2(self):
        pass

class TestPaperA(TestPaper):
    def answer1(self):
        return "A"

    def answer2(self):
        return "B"

class TestPaperB(TestPaper):
    def answer1(self):
        return "C"

    def answer2(self):
        return "D"

def main():
    student_a = TestPaperA()
    student_a.question1()
    student_a.question2()
    student_b = TestPaperB()
    student_b.question1()
    student_b.question2()

if __name__ == '__main__':
    main()