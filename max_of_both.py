# Program to set two numbers to highest value

n = int(input("Enter First Number : "))
m = int(input("Enter Second Number : "))

if n > m:
    m = n
else:
    n = m

print(f"n = {n} , m = {m}")
