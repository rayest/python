# coding=utf-8
# 设置编码

import math
# module introduce
import introduce

print ("不换行"),
print ("换行")
print ("end")

# 字符串
description = 'ILovePython'
print description
print description[2]
print description[2:]
print description[2:5]
print description * 2

# 列表
lists = [1, 2, 3, 4, 'ray', 'Lee', 5]
print lists
print lists[2]

# 字典
dicts = {'name': 'john', 'code': 6734, 'dept': 'sales'}
dicts.pop('code')
print dicts.keys()
print dicts.values()
print dicts['name']

a = 5
b = 6
print a != b
if a and b:
    print 'true'
else:
    print '有一个不为true'

# in and is  is not
c = 10
d = 11
list2 = [1, 2, 3, 4, 5, 10]
print c in list2
print c is d

# while 循环
number = 0
while number < 10:
    number += 1
print number

# for 循环
for letter in 'Rayest lee':
    print letter

names = ['Ray', 'Lee', 'Rayest']
for index in range(len(names)):
    print names[index]


# function
def say():
    return "Hello"


print say()

# lambda function
sumss = lambda number1, number2: number1 + number2
result = sumss(10, 20)
print result

print introduce.minus(20, 10)


def computePrice(total):
    if total < 10:
        print total * 10
    elif (total >= 10) & (total < 50):
        print total * 8
    else:
        print total * 5


computePrice(3)

print math.cos(60)


# 可变参数
def computeChanges(*scores):
    sums = 0
    for score in scores:
        sums = sums + score
    print sums


computeChanges(1, 2, 3, 4, 5, 6)

for x, y in [(1, 2), (3, 4), (5, 6)]:
    print x, y


# Python内建了map()和reduce()函数。将传入的函数依次作用到序列的每个元素
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))


# Python内建的filter()函数用于过滤序列。根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n % 2 == 1


r2 = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r2))

# Python内置的sorted()函数就可以对list进行排序：
print(sorted([1, 9, 4, 5, 4, 7, 9, 3, 0, 3]))
print(sorted([1, 3, 0, -2, 9, 5, -8, 3, 6, -5]))
print(sorted([1, 3, 0, -2, 9, 5, -8, 3, 6, -5], key=abs))
print(sorted(["Wnei", "wnei g", "wnei c", "wnej", "Anei", "wnei"]))
print(sorted(["Bnei", "anej", "Cnei", "wnei"], key=str.lower))
print(sorted(["Bnei", "anej", "Cnei", "wnei"], key=str.lower, reverse=True))


# 匿名函数
# 关键字lambda表示匿名函数，冒号前面的m表示函数参数。只能有一个表达式
xy = lambda m: m * m
print(xy(3))