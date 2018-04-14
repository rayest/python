# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数

def validate(func):
    def wrapper(username):
        print('验证参数:', username)
        return func(username)
    return wrapper


@validate
def login(username):
    print('登陆成功')


# validate(login)
login('lee')
