roman = 'ivxlcm'
num = input()


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


def div(r):
    for i in r:
        if i not in roman:
            return False
    r += '  '
    l = []
    i = 0
    while i < len(r) - 1:
        if res(r[i]) < res(r[i + 1]):
            if res(r[i + 1]) < res(r[i + 2]):
                return False
            l.append(r[i:i + 2])
            i += 2
        else:
            l.append(r[i])
            i += 1
    l.pop()
    return l


def fin(result):
    if not result:
        return 'Invalid Number'
    s = 0
    for i in result:
        if len(i) == 1:
            s += res(i)
        else:
            s += (res(i[1]) - res(i[0]))
    return s


print(fin((div(num))))
