l = []
for i in range(int(input())):
    a = int(input())
    b = int(input())
    c = int(input())
    m = int(input())
    p = int(input())
    s = (a ** b) ** c
    if s % m == 0:
        l.append('No 0')
    else:
        l.append('Yes ' + str(s * p))

for i in l:
    print(i)
