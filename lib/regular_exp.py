# Program to display lines of the given file containing at least one digit

import re

with open("numbers.txt", "rt") as r:
    for i in r:
        if re.search("\d+", i):
            print(i.strip("\n"))
