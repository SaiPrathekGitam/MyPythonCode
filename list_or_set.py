# Program to check whether the object is a list or a set

names = []
s = set()


def add(lst=[]):
    lst.append(2)
    print(lst)


add(names)
names.append(input("Enter The Name"))
print(names)
