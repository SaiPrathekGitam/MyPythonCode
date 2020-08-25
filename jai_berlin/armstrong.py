n, a = int(input()), 0
for i in str(n):
    a += int(i) ** len(str(n))
print(a == n)
