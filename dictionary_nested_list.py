# Program to display given names and all numbers for the name in sorted order

num = list()
name = list()

name.append(input("Enter The Name ('end' to stop) : "))
num.append(input("Enter The Number : "))

while True:
    name.append(input("Enter The Name ('end' to stop) : "))
    if name[-1] == 'end':
        break
    if name.count(name[-1]) > 1:
        num.insert(name.index(name[-1]), [num.pop(name.index(name[-1])), input("Enter The Number : ")])
    elif name.count(name[-1]) > 2:
        num.insert(name.index(name[-1]), [num.pop(name.index(name[-1])), input("Enter The Number : ")])
    else:
        num.append(input("Enter The Number : "))

data = dict(zip(name, num))
for i in data:
    print(i, data[i])

print()
print(data.items())
