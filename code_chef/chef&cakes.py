from itertools import permutations

s = set()
for i in range(int(input())):
    n = int(input())
    num = map(int, input().split())
    nums = ''
    for j in num:
        nums += str(j)
    for p in permutations(nums):
        num = ''
        for k in p:
            num += k
        s.add(int(num))
    for p in permutations(nums):
        print(p)

print(sum(s))
