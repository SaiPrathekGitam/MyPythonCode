string = input()
sc = dc = spc = 0
for i in string:
    if i.isnumeric():
        dc += 1
    elif not i.isalpha():
        spc += 1
    else:
        sc += 1
print(sc, dc, spc)
