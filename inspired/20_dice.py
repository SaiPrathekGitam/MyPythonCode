# Program to simulate a dice
import random


class RandomException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


d = {i: 0 for i in range(100)}
for i in range(100):
    while True:
        dice1 = random.randint(1, 7)
        dice2 = random.randint(1, 7)
        if dice1 == dice2:
            # print('Yay', dice2)
            break
        else:
            d[i] += 1

for i, j in sorted(d.items()):
    print(i, j)
