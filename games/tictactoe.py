# tic tac toe
import random

buds = []
tics = [i for i in range(1, 10)]
while True:
    while True:
        num = random.randint(1, 9)
        if num not in buds:
            buds.append(num)
            break
    if len(buds) == 9:
        break


def mp(rix):
    for i in range(9):
        print(rix[i], end=' ')
        if (i + 1) % 3 == 0:
            print()


def check(rix):
    rix.append(-1)
    rix.append(-2)
    if rix[0] == rix[4] and rix[0] == rix[8]:
        return True
    if rix[2] == rix[4] and rix[2] == rix[6]:
        return True
    for i in range(9):
        if i % 3 == 0 and rix[i] == rix[i + 1] and rix[i] == rix[i + 2]:
            return True
        if i < 3 and rix[i] == rix[i + 3] and rix[i] == rix[i + 6]:
            return True
    return False


chance = 0
while chance < 9:
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
    if check(tics):
        if chance % 2 == 0:
            print('Comp')
        else:
            print('User')
        break
    chance += 1
else:
    print('Tie')