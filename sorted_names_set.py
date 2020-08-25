# Program to sort the unique names given by the user

name = input("Enter The Name : ")
names = set()

while True:
    if name == "end":
        break
    else:
        names.add(name)
        name = input("Enter The Name : ")

print("\nThe names in the sorted order :")

print(sorted(names))
