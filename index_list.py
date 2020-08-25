# Program to display list values along with their index
name = input("Enter The Name : ")
names = []

while True:
    if name == "end":
        break
    else:
        names.append(name)
        name = input("Enter The Name : ")

for i in enumerate(names):
    print(i)
