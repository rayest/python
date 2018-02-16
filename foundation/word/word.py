def filter_text(x):
    with open(x, 'r') as f:
        text = f.read()
        userinput = input('myinput:')
        for i in text.split('\n'):
            if i in userinput:
                userinput = userinput.replace(str(i), '*' * len(i))
        print(userinput)


if __name__ == '__main__':
    filter_text('word.txt')
