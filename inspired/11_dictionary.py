# Program to illustrate dictionaries

# d = {'python': 3.7, 'java': 12, 'vb': 14}
# print(d['python'])

# for k in d:
#     print(k, d[k])

# for t in d.items():
# print(t)

# for t in sorted(d.items()):
#     print(t)

# d = {}
# while True:
#     name = input("Enter Name : ")
#     if name == 'end':
#         break
#     else:
#         num = int(input("Enter Mobile Number : "))
#         d[name] = num
#
# for i in sorted(d):
#     print(i, d[i])

# d = {}
# while True:
#     name = input("Enter Name : ")
#     if name == 'end':
#         break
#     num = int(input("Enter Mobile Number : "))
#     elif name in d:
#         d[name].append(num)
#     else:
#         d[name] = [num]
# for i in sorted(d):
#     print(i, d[i])

# d = {}
# s = input('Enter String : ')
# for i in s:
#     if i in d:
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
#
# print(d.items())

# ============================================ Dictionary Comprehension ============================================

# sqrs = {n:n*n for n in range(1, 11)}
# print(sqrs)

# s1 = {123, 312, 423, 123}
# s2 = {13, 12, 43, 12}
# d = dict(zip(s1, s2))
# print(d)

# ============================================ Word Frequency ======================================================

d = {}
line = input("Enter String : ")
line += ' '
word = ''
for i in line:
    if i.isalpha():
        word += i
    else:
        if word in d:
            d[word] += 1
            word = ''
        else:
            d[word] = 1
            word = ''

for i in d:
    print(i, d[i])
