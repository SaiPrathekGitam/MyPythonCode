string = input()
a = []
s = ''
for i in string:
    if i.isnumeric():
        s += i
    elif len(s) != 0:
        a.append(int(s))
        s = ''

print(sum(a) % int(s))
