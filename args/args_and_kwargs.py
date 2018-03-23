# 接收参数列表
def test_args(param, *args):
    print('normal arg: ', param)
    for arg in args:
        print('arg from args: ', arg)


# 接收键值对列表
def test_kwargs(param, **kwargs):
    print('normal arg: ', param)
    for key, value in kwargs.items():
        print('{0}=={1}'.format(key, value))


if __name__ == '__main__':
    print(test_args(1, 2, 3, 4))
    print(test_kwargs(1, number='2', age=25))
