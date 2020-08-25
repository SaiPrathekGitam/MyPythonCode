d = {}
while True:
    n = int(input())
    if n == 0:
        break
    m = int(input())
    if n in d:
        d[n] += m
    else:
        d[n] = m

for i, v in d.items():
    print(i, '-', v)
