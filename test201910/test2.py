def max_get():
    try:
        a = [input(), input(), input()]
        print(max(a))
    except ValueError:
        print("输入有误")

if __name__ == '__main__':
    max_get()
