#  Program to validate and the increment the given date

while True:

    date = input("Enter The Date In (DD/MM/YYYY) Format : ")

    if date == "end":
        break

    dd, mm, yy = date.split('/')

    if len(yy) != 4:
        print("Invalid Date")

    dd = int(dd)
    mm = int(mm)
    yy = int(yy)

    check = -1

    if yy >= 400:  # Checking for leap year
        if yy % 100 is 0:
            if yy % 400 is 0:
                check = 1
        elif yy % 4 is 0:
            check = 1

    if dd <= 0 or 0 >= mm > 12 or yy <= 0:
        print("Invalid Date")

    if mm % 2 == 0 and mm > 2:
        max = 30
        if dd > 30:
            print("Invalid Date")
    elif mm == 2 and check == 1:
        max = 29
        if dd > 29:
            print("Invalid Date")
    elif mm == 2 and check == -1:
        max = 28
        if dd > 28:
            print("Invalid Date")
    else:
        max = 31
        if dd > 31:
            print("Invalid Date")

    print(f"The Entered Date is {dd} / {mm} / {yy}")

    days = int(input("Enter the number of days to be added : "))

    for i in range(1, days + 1):
        if dd < max:
            dd += 1
        elif dd == max and mm != 12:
            dd = 1
            mm += 1
        elif dd == max and mm == 12:
            dd = 1
            mm = 1
            yy += 1

    print(f"The Incremented Date is {dd} / {mm} / {yy}")
