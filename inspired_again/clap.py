def clap(num):
    if num % 3 == 0:
        return True
    for i in str(num):
        if i in '369':
            return True
    return False


claps =  []
for i in range(int(input())):
    if clap(i + 1):
        claps.append('clap')
    else:
        claps.append(i + 1)

print(claps)