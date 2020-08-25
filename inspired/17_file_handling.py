# Program to illustrate file handling

# with open('names.txt', 'rt') as f:
#     names = f.readlines()
#
# for m in range(len(names)):
#     names[m] = names[m].split(',')
#
# new = []
# for i in names:
#     new.append(i[0])
#
# print(new)

# names = open('names.txt', 'rt')
# s = set()
# for i in names.readlines():
#     st = i.split(',')[0]
#     s.add(st)
# print(sorted(s))


def add(s):
    m = s.split(',')
    m[-1] = m[-1].rstrip('\n')
    for j in m:
        if not j.isnumeric():
            m.remove(j)
    for j in m:
        m[m.index(j)] = int(j)
    return sum(m)


names = open('names.txt', 'rt')
for i in names.readlines():
    print(i.partition(',')[0].ljust(10), '-', add(i.partition(',')[2]))
