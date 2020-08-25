a = []
for i in range(1, 11):
    n = int(input())
    if n % 2 == 0:
        a.insert(0, n)
    else:
        a.append(n)
print(a)
