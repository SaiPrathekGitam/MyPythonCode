# Program to find largest number entered by the user, stop at zero

maxi = int(input("Enter Numbers [0 To Stop] : "))
while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num > maxi:
            maxi = num
print(maxi)
