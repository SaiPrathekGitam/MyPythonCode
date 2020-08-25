# Program to check whether entered number is prime or not
num = int(input("Enter A Number : "))
for i in range(2, num // 2 + 1):
    if num % 2 == 0:
        print("Composite.")
        break
else:
    print("Prime")
