# Program to find out whether given number is prime or not

n = int(input("Enter The Number : "))

for i in range(2, n // 2):
    if n % i == 0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")
