import random, string

forSelect = string.ascii_letters + "0123456789"


def generate(count, length):
    for x in range(count):
        re = ""
        for y in range(length):
            re += random.choice(forSelect)
            print(re)


if __name__ == "__main__":
    generate(2, 5)
