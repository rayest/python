import random


def test():
    a = ''
    for i in range(4):
        a = a + str(random.randint(0, 9))
    print(a)


if __name__ == '__main__':
    test()
