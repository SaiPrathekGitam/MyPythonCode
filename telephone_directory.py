d = {}

while True:
    name = input("Enter The Name ('end' to stop) : ")
    if name == 'end':
        break
    num = input("Enter The Mobile Number : ")
    if name in d:
        d[name].add(num)
    else:
        d[name] = {num}

print(sorted(d.items()))
