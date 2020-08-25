s = input()
count = 0
for i in s:
    if i == '(':
        count += 1
    elif i == ')':
        count -= 1
    if count < 0:
        print(False)
        break
else:
    print(True)
