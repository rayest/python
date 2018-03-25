pass_line = 60

'''
1.  闭包：内函数里运用了外函数的临时变量，
    并且外函数的返回值是内函数的引用。
2.  如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，
    就把这个临时变量绑定给了内部函数，然后自己再结束
'''


def check_if_pass(score):
    print('%x' % id(score))
    print('pass') if score >= pass_line else print('not pass')

    def in_func():
        print(score)

    return in_func


if __name__ == '__main__':
    f = check_if_pass(90)
    f()
    print(f.__closure__)
