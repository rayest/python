
def scientific_notation_to_float(x):
    y = '{:.8f}'.format(float(x))  # 5f表示保留5位小数点的float型
    print (y)


if __name__ == '__main__':
    scientific_notation_to_float('1.3e-5')
