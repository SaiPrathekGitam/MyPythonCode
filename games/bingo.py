from random import randint

l = []
count = 0
print("Enter 25 numbers")
while True:
    if count == 25:
        break
    # a = int(input(f"Enter Number {count + 1} : "))
    a = randint(1, 25)
    if a in l:
        print("",end="")
        # print("Number already Entered")
    elif 25 < a:
        print("Please Enter A Number Between 1 and 25")
    elif 1 > a:
        print("Please Enter A Number Between 1 and 25")

    else:
        l.append(a)
        l.append(a)
        count += 1

for i in range(1, 26):
    if i % 5 == 0:
        print(l[i - 1])
    else:
        print(l[i - 1], end=' ')
