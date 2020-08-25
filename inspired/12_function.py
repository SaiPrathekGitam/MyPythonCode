# Program to illustrate functions


# def a():
#     return 1
#
#
# print(a())
#
#
# def add(a, b):
#     return a + b
#
#
# print(add(10, 20))
# print(add('KS', ' Prathek'))


# =========================================== Default Argument Values ==============================================


# def print_msg(msg, count=1):
#     for i in range(1, count + 1):
#         print(msg)
#
#
# print_msg('yo')
# print_msg('mama', 5)
#
# print_msg(count=2, msg='hey')


# def rev_str(a):
#     print(a[::-1])
#
#
# rev_str('reverse')


# def rev_str(a, case='s'):
#     if case == 'u':
#         print(a[::-1].upper())
#     elif case == 'l':
#         print(a[::-1].lower())
#     else:
#         print(a[::-1])
#
#
# rev_str('Reverse')
# rev_str('Reverse', 'u')
# rev_str('Reverse', 'l')


# def list_pos(l1, l2):
#     for i in l1:
#         if i in l2:
#             print(l2.index(i), end=' ')
#         else:
#             print('nf', end=' ')
#
#
# la = [1, 3, 5]
# lb = [4, 3, 2]
# list_pos(la, lb)


# def add(*nums):
#     return sum(nums)
#
#
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))


# def add(*nums, msg = 'sum'):
#     print(msg, sum(nums))
#
#
# add(1, 2, msg = 'Total')
# add(1, 2, 3)
# add(1, 2, 3, 4, msg = 'Sum')


# def show(**details):
#     print(details)
#
#
# show(a=10, b=10, c=30)


# def fun1():
#     print('In fun1()')
#
#
# def fun2():
#     print('In fun2()')
#
#
# fun1 = fun2
# fun1()


# def s(a, b):
#     return a + b
#
#
# def m(a, b):
#     return a * b
#
#
# def math_op(fun, a, b):
#     print(fun(a, b))
#
#
# math_op(s, 10, 20)
# math_op(m, 10, 20)

# =============================================== Lambda Functions ==================================================


# def iseven(n):
#     return n % 2 == 0
#
#
# nums = [1, 2, 3, 5, 6, 7, 9]
# evens = filter(iseven, nums)
# evens2 = filter(lambda n: print(n), nums)
# for i in evens2:
#     print(i)

# names = []
# while True:
#     name = input()
#     if name == 'end':
#         break
#     names.append(name)
#
# names = sorted(names, key=len)
# names = sorted(names, key=str.upper)
# names = sorted(names, key=lambda n:n[-2:])
# print(names)

# ==================================== Pass By ========================================


# def fun(x):
#     print(id(x))
#     x = 20
#     print(id(x))
#
#
# a = 10
# print(id(a))
# fun(a)
# print(id(a))


# def swap(a, b):
#     a, b = b, a
#
#
# x, y = 10, 20
# print(x, y)
# swap(x, y)
# print(x, y)


# ======================================== Scope Functions =======================================

# v1 = 10
#
#
# def fun1():
#     v2 = 20
#     print('fun1()')
#
#     def fun2():
#         nonlocal v2
#         v2 += 10
#         print(v1, v2)
#
#     fun2()
#
#
# fun1()
# =========================================== Import ===============================================
import math as m

print(m.sqrt(2))
