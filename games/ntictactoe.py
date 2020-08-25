# tic tac toe
import random

n = int(input())
p = n ** 2
buds = []
tics = [i for i in range(1, p + 1)]
while True:
    while True:
        num = random.randint(1, p)
        if num not in buds:
            buds.append(num)
            break
    if len(buds) == p:
        break


def mp(rix):
    for i in range(p):
        print(rix[i], end=' ')
        if (i + 1) % n == 0:
            print()


def ncheck(rix):
    bulb = True
    for i in range(n):
        rix.append(-i)
    for i in range(n):
        for j in range(n):
            if rix[0] != rix[j]:
                bulb = False
    return bulb
    for i in range(0, p, n + 1):
        if rix[0] != rix[i]:
            bulb = False
    return bulb
    for i in range(n - 1, p - n, n - 1):
        if rix[n - 1] != rix[i]:
            bulb = False
    return bulb


for i in range(0, p, n + 1):
    print(i + 1, end=' ')
print()
for i in range(n - 1, p - n + 1, n - 1):
    print(i + 1, end=' ')
#     for i in range(9):
#         if i % 3 == 0 and rix[i] == rix[i + 1] and rix[i] == rix[i + 2]:
#             return True
#         if i < 3 and rix[i] == rix[i + 3] and rix[i] == rix[i + 6]:
#             return True
#     return False


chance = 0
while chance < p:
    if chance % 2 == 0:
        comp = buds.pop()
        print(comp)
        tics[comp - 1] = 'X'
        mp(tics)
    else:
        while True:
            user = int(input())
            if user in buds:
                del buds[buds.index(user)]
                break
        tics[user - 1] = 'O'
    if ncheck(tics):
        if chance % 2 == 0:
            print('Comp')
        else:
            print('User')
        break
    chance += 1
else:
    print('Tie')
