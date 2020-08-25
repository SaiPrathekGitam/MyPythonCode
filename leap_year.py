# Program to check if the given year is a leap year

n = int(input("Enter The Year : "))
check = -1

while True:
    if n >= 400:
        if n % 100 is 0:
            if n % 400 is 0:
                check = 1
        elif n % 4 is 0:
            check = 1

    if check == 1:
        print(f"{n} is a Leap Year")
    else:
        print(f"{n} is not a Leap Year")

    n = int(input("Enter The Year : "))

    if n == 0:
        break
