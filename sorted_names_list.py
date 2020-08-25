# Program to sort the names given by the user

name = input("Enter The Name : ")
names = []

while True:
    if name == "end":
        break
    else:
        names.append(name)
        name = input("Enter The Name : ")

print("\nThe names in the sorted order :")

print(sorted(names))
