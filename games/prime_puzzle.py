# swap tiles until no prime numbers are adjacent

import random
from itertools import islice
import math

n = int(input())
p = n ** 2

buds = []
while len(buds) != p:
    while True:
        num = random.randint(1, p)
        if num not in buds:
            buds.append(num)
            break


def check(m):
    if m == [i for i in range(1, p)]:
        return False
    return True


pad = len(str(p))
while check(buds):
    for i in range(p):
        print(str(buds[i]).rjust(pad, '0'), end=' ')
        if (i + 1) % n == 0:
            print()

    a, b = int(input()), int(input())
    an, bn = buds.index(a), buds.index(b)
    if abs(an - bn) == n or abs(an - bn) == 1:
        temp = buds[an]
        buds[an] = buds[bn]
        buds[bn] = temp
    else:
        print('no')

for i in range(p):
    print(str(buds[i]).rjust(pad, '0'), end=' ')
    if (i + 1) % n == 0:
        print()
print('Noice!')
