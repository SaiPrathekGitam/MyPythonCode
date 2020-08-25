# Program to enter numbers in a list left if number is odd (in order) and right if number is even

num = []
count = 0

for i in range(10):
    n = int(input("Enter The Number : "))
    if n % 2 == 0:
        num.append(n)
    else:
        num.insert(count, n)
        count += 1

print(num)
