def rotate(num):
    num = str(num)
    t = num[0]
    for i in range(1, len(num) - 1):
        num[i] = num[i + 1]
    num[-1] = t
    return int(num)


def prime(num):
    for i in range(3, num // 2):
        if num % i == 0:
            return False
    return True


n = int(input())
for i in range(len(str(n))):
    if not prime(n):
        print("Not R Prime")
        break
    n = rotate(n)
else:
    print("R Prime")
