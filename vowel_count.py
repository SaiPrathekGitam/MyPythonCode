# Program to count the number of vowels present in the given string
count = 0

n = input("Enter The String : ")
check = set('AaEeIiOoUu')

for i in n:
    if i in check:
        count += 1

print(f"There are {count} vowels in the String '{n}'")
