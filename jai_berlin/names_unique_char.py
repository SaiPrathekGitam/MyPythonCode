string = input()
s = set()
while string != 'end':
    for i in set(string):
        s.add(i)
    string = input()
print(s)
