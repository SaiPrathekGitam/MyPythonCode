a, b = int(input()), int(input())
if a > b:
    min1 = a
else:
    min1 = b
if a == 0 or b == 0:
    print('Not Non Zero')
else:
    while True:
        if min1 % a == 0 and min1 % b == 0:
            print(min1)
            break
        min1 += 1
