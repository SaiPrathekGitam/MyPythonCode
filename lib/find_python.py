# Program to display all python files in the given folder

import os

files = os.walk(r"C:\Python")
for f, g, h in files:
    for i in h:
        if i[-3:] == ".py":
            print(i)

