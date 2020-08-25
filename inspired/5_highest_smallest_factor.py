# Program to find highest factor
num = int(input("Enter A Number : "))
for n in range(num // 2, 0, -1):
    if num % n == 0:
        print(n)
        break

for i in range(2, n//2 + 1):
    if num % n == 0:
        print(n)
        break
else:
    print(num)
