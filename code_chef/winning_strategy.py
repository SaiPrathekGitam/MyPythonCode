n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

s = f = 0
for i in range(n):
    if (i + 1) % 2 != 0:
        f += l[i]
    else:
        s += l[i]

ss = sf = 0
for i in range(n):
    if n == 1:
        break
    temp = l[0]
    l[0] = l[1]
    l[1] = temp
    if (i + 1) % 2 == 0:
        sf += l[i]
    else:
        ss += l[i]

if max(ss, sf) < max(s, f):
    if s < f:
        ch = 'First'
    elif s > f:
        ch = 'Second'
    else:
        ch = 'Draw'
else:
    if ss < sf:
        ch = 'First'
    elif ss > sf:
        ch = 'Second'
    else:
        ch = 'Draw'
print(ch)
