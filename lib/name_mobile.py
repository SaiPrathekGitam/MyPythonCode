# Program to print names and mobile numbers from person.txt

import re

names = {}
with open("persons.txt", "rt") as file:
    for all in file:
        name = re.findall("[A-Za-z]+", all)
        number = re.findall("[\d]+", all)
        new = ""
        for j in name:
            new += " " + j
        names[new] = number

for i, j in sorted(names.items()):
    if i != "":
        print(i.strip(" ").ljust(20), ":", j)
    # else:
    #     print("Invalid Entry")
