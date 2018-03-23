class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score


if __name__ == '__main__':
    student = Student('lee', 100)
    print(student.name)
    print(student.score)
    student.score = 99
    print(student.score)
