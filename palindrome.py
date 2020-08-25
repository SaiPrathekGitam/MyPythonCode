# Program to check if the given number is a Palindrome Number

n = input("Enter The Number : ")

if n == n[::-1]:
    print(f"{n} is a Palindrome Number")
else:
    print(f"{n} is not a Palindrome Number")
