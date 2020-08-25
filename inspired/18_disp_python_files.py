# Program to display python files in the given folder

import os

files = os.walk(r'c:\python\langdemo\inspired_again')

s = set()
for f, g, h in files:
    for i in h:
        if i[-2::] == 'py':
            s.add(i)

for i in s:
    print(i)
