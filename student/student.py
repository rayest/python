class Student(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


student = Student('lee')
print(student.get_name())


def get_square(x, y):
    _, t = x * x, y * y
    print(type(t))
    print(t)
    return t


if __name__ == '__main__':
    get_square(2, 3)
