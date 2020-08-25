# Program to create random pairs

from random import randint
import sys
import os

os.system('cls')
while True:
    r = int(input("Enter The Number Of Players : "))
    x = int(input("Enter Number Of Teams : "))
    lst = []  # ['a', 'b', 'c', 'd', 'e', 'f']
    s = []
    for i in range(1, r + 1):
        lst.append(i)
    while len(s) != len(lst):
        n = randint(1, len(lst))
        if n in s:
            continue
        else:
            s.append(n)

    if len(lst) % x != 0:
        while True:
            os.system('cls')
            ans = input(f"{len(lst) % x} Player(s) Will Be Left. Do You Want To Enter The Details Again(y/n)?")
            if ans[0] == 'y' or ans[0] == 'Y':
                break
            elif ans[0] == 'n' or ans[0] == 'N':
                sys.exit()
    else:
        n = len(lst) // x
        count = 0
        team = 1

        for i in s:
            if count % (n) == 0:
                if team == x + 1:
                    print(f"\n\nSorry! {len(lst) - count} player(s) left....")
                    break
                print(f"\nTeam {team} : ", end="")
                team += 1
            print(lst[i - 1], end=" ")
            count += 1
        break
