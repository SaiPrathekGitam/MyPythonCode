def convert(num, base):
    count = 0
    while num != 0:
        count += 1
        num //= base
    return count


for i in range(int(input())):
    number = int(input()) ** int(input())
    for j in range(2, 21):
        print(convert(number, j), end=' ')
