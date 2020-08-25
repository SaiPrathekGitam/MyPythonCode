roman = 'ivxlcm'
num = input('Enter The Roman Numeral : ')


def res(r):
    if r == 'i':
        return 1
    if r == 'v':
        return 5
    if r == 'x':
        return 10
    if r == 'l':
        return 50
    if r == 'c':
        return 100
    if r == 'm':
        return 1000
    return 0


def check(r):
    for it in roman:
        if it not in r:
            return False


s = 0
for i in num:
    s += res(i)

print(s)
