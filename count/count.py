# coding = utf-8
import re


def count(path):
    with open(path, 'r') as files:
        data = files.read()
        print(data)
        words = re.compile('[a-zA-Z0-9]+')
        dict_counts = {}
        for x in words.findall(data):
            if x not in dict_counts:
                dict_counts[x] = 1
            else:
                dict_counts[x] += 1
        print(dict_counts)


if __name__ == '__main__':
    count('count.txt')
