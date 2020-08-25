# Program to find highest and smallest factor of given number

n = int(input("Enter the number : "))

for i in range(n // 2 + 1, 1, -1):
    if n % i == 0:
        print(f"{i} is the highest factor of {n}")
        break
else:
    print("prime")

for i in range(2, n // 2 + 1):
    if n % i == 0:
        print(f"{i} is the smallest factor of {n}")
        break
