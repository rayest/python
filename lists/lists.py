def change_name():
    name = 'rayest'
    if name[-3:] == 'est':
        name = 'lee'
    print(name[:3] + '-' + name[3:])


if __name__ == '__main__':
    change_name()
