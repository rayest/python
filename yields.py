def fab(max):
    i = 0
    while i < max:
        yield i
        i = i + 1


def get_number():
    for n in fab(5):
        print(n)


if __name__ == '__main__':
    get_number()
