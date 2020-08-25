# Program to print names from bad_names.txt.txt

import re

with open("bad_names.txt", "rt") as file:
    for i in file:
        for j in re.findall("[A-za-z]+", i):
            print(j)
