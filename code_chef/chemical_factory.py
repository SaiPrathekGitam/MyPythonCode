l = []

for i in range(int(input())):
    n, k1, k2 = map(int, input().split())
    p1, p2, p3, p4 = map(int, input().split())
    l = [-1 for i in range(n)]
    for j in range(k1, k2 + 1):
        for k in range(len(l)):
            if (k + 1) % j == 0:
                l[k] += 1
    s = 0
    for j in l:
        if j == 2:
            s += p1
        elif j % 2 == 1:
            s += p2
        else:
            s += p3

    print(s)
