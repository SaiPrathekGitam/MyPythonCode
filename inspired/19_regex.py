# Program to illustrate regular expressions

import re

# a = 'abc'
# d = '12,34'
# print(re.match('[a-z]+', a))
# print(re.match('[a-z]+', 'bc1234'))
# print(re.match('[^0-9a-z]', 'ABCDEF'))
# print(re.match('\d+', d))
# print(re.match('\d*', d))
# print(re.match('\d?', d))
# print(re.search('\d+', d))

# with open('names.txt', 'r') as file:
#     lines = file.readlines()
#
# for l in lines:
#     if re.search('\d+', l):
#         print(l, end='')

# m = re.findall('\d+', 'This is 100, 200')
# print(type(m))
# m = re.search('\d+', 'This is 100, 200')
# print(m)
# print(type(m))
# print(m.span())
# print(m.group())
# print(m.start())
# print(m.end())

# with open('names.txt', 'r') as file:
#     lines = file.readlines()
#
# names = set()
# for i in lines:
#     line = re.split('[,:; ]+', i)
#     for j in line:
#         j = j.rstrip('\n')
#         # print(j, end=' ')
#         if j != '':
#             names.add(j)
#
# # print(names)
# for i in names:
#     print(i)

from datetime import datetime

d = datetime.strptime('04-05-2020', 'dd-mm-yyyy')
print(d)