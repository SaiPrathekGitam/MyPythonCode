m = []

for i in range(10):
    m.append(int(input()))

avg = sum(m) / 10

for i in m:
    if i > avg:
        print(i, end=' ')
