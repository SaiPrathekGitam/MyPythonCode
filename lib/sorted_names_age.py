# Program to print names and ages from names_DOB.txt.txt in sorted order

from datetime import datetime

names = {}
with open("names_DOB.txt", "rt") as file:
    for line in file:
        name, date = line.split(" ")
        # print(name.ljust(13),date.strip("\n"))
        d1 = datetime.now()
        d2 = datetime.strptime(date.strip("\n"), "%Y-%m-%d")
        age = d1 - d2
        names[name] = age

for i in sorted(names, key=names.get):
    print(i.ljust(12), ":", names[i])
