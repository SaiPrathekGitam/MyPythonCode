# Program to  illustrate lists

# l = [45, 2, 3, 65, 43, 23]
# print(l, type(l))

# for i in l:
#     print(i)

# l[0] = 10
# print(l[-1])
# l.append(20)
# l.insert(0, 100)
# l.extend([100, 200])
# l1 = [1, True, 'abc']
# l.remove(100)
# del l[0]
# print(l.pop())
# print(dir(list))
# print(l.index(2))
# print(l)

# names = []
# names.append('Java')
# names.append('Python')
# print(sorted(l))                                  copy
# print(l)
# l.sort()                                            modifies original
# print(l)
# print(names)

# l = []
# while True:
#     i = input()
#     if i == 'end':
#         break
#     l.append(i)
# print(sorted(l))

# l = []
# for i in range(1, 11):
#     n = int(input())
#     if n % 2 == 0:
#         l.append(n)
#     else:
#         l.insert(0, n)
# print(l)

# ================================================= LIST COMPREHENSION ================================================

# o = []
# e = []
# for i in range(1, 11):
#     n = int(input())
#     if n % 2 == 0:
#         e.append(n)
#     else:
#         o.append(n)
# print(o + e)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i, v in enumerate(l):
    print(i, '-', v)

# l2 = ['a', 'b', 'c', 'd']
# for i, p in zip(l, l2):
#     print(i, p)