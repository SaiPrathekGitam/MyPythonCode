def skips(a):
    l = [0]
    asum = 0
    a1 = 0
    while (asum < a + 1):
        l.append(asum)
        a1 += 1
        asum = 2 ** a1 - 1
    return l


def check(a):
    a += 1
    count = 0
    # b = 0
    while (True):
        l = skips(a)
        a -= (l[-1] + 1)
        if a <= 0:
            break
        count += 1
    return count


for i in range(int(input())):
    a, b = int(input()), int(input())
    if check(a) == check(b):
        print(0, end=' ')
    elif check(a) > check(b):
        print(2, end=' ')
    else:
        print(1, end=' ')
    print(abs(check(a) - check(b)))
