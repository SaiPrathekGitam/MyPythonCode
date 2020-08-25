# swap tiles until no prime numbers are adjacent

import random
from itertools import islice
import math

buds = []
while len(buds) != 9:
    while True:
        num = random.randint(1, 9)
        if num not in buds:
            buds.append(num)
            break


def pb(trix):
    for i in trix:
        for j in i:
            print(j, end=' ')
        print()


def prime(n1, n2):
    num = n1 + n2
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            swap(n1, n2)


def swap(i, j):
    temp = nb[i][j]
    nb[i][j] = nb[i + 1][j]
    nb[i + 1][j] = temp


it = iter(buds)
nb = [list(islice(it, 3)) for i in range(3)]
pb(nb)

for j in range(5):
    for i in range(9):
        print(buds[i], end=' ')
        if (i + 1) % 3 == 0:
            print()

    a, b = int(input()), int(input())
    an, bn = buds.index(a), buds.index(b)
    if abs(an - bn) == 3 or abs(an - bn) == 1:
        temp = buds[an]
        buds[an] = buds[bn]
        buds[bn] = temp
    else:
        print('no')

for i in range(9):
    print(buds[i], end=' ')
    if (i + 1) % 3 == 0:
        print()
# for i in range(2):
#     for j in range(2):
#         if prime(nb[i][j], nb[i + 1][j]):
#             swap(i, j)
print()
# pb(nb)
