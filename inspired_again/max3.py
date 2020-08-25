s = input()
flag = True
for i in s:
    if i != '3' and flag:
        print(3, end='')
        flag = False
    else:
        print(i, end='')
