def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


if __name__ == '__main__':
    print(10 / 3)
