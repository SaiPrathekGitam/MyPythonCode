l = ['qwe', 'Qdef', 'sfQfsf', 'WESFD']


def up(s):
    for j in s:
        if j.isupper():
            return True
    return False


for i in filter(up, l):
    print(i, end=' ')
