# Program to find largest of the entered numbers
n = int(input("Enter Number : "))
maximum = 0

if n >> maximum:
    maximum = n

while n != 0:
    n = int(input("Enter Number : "))
    if n > maximum:
        maximum = n

print(f"Maximum Number is {maximum}")
