# Program to enter numbers in a list left if number is odd and right if number is even

num = []

for i in range(10):
    n = int(input("Enter The Number : "))
    if n % 2 == 0:
        num.append(n)
    else:
        num.insert(0, n)

print(num)
