def fun(num):
    print(len(str(num)))
    s = 0
    for i in str(num):
        s += int(i)
    print(s)


fun(int(input()))
