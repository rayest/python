import urllib.request


def run():
    file = urllib.request.urlopen("http://www.baidu.com")
    data = file.read()
    print(data)
    data_line = file.readline()
    print(data_line)


if __name__ == '__main__':
    run()
