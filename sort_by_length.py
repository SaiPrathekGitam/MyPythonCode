# Program to sort given strings in the list by length

names = []

while True:
    name = input("Enter The Name ('end' to stop): ")
    if name == 'end':
        break
    names.append(name)

names.sort()
names.sort(key=len)
print(names)
