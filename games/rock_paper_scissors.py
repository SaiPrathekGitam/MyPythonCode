from random import randint

print(
    "Rules : \n1. Enter 1 for Rock, 2 for Paper and 3 for Scissors, and press Enter.\n2. First to reach 5 points Wins!")
count1 = count2 = 0
g = ("Rock  💎  ", "Paper  📃  ", "Scissors  ✂ ")
while True:
    print()
    if count1 == 5 or count2 == 5:
        break
    if count1 == count2:
        print(f"Tied at {count1} to {count2}")
    if count1 > count2:
        print(f"You are winning by {count1} to {count2}")
    if count2 > count1:
        print(f"You are losing by {count1} to {count2}")

    ans = int(input("Enter : "))
    ans = ans - 1
    c = randint(0, 2)
    print(f"The Computer Chose {g[c]}")

    if ans == c:
        print("No one gets a point")
    elif ans == 0 and c == 1:
        print(f"Sorry!{g[c]} beats {g[ans]}")
        count2 += 1
    elif ans == 0 and c == 2:
        print(f"Yay!{g[ans]} beats {g[c]}")
        count1 += 1
    elif ans == 1 and c == 2:
        print(f"Sorry!{g[c]} beats {g[ans]}")
        count2 += 1
    elif ans == 1 and c == 0:
        print(f"Yay!{g[ans]} beats {g[c]}")
        count1 += 1
    elif ans == 2 and c == 0:
        print(f"Sorry!{g[c]} beats {g[ans]}")
        count2 += 1
    elif ans == 2 and c == 1:
        print(f"Yay!{g[ans]} beats{g[c]}")
        count1 += 1

if count1 > count2:
    print("You Win")
else:
    print("You Lose")
