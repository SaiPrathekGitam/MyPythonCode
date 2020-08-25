nums = []
for i in range(int(input())):
    nums.append(int(input()))

s = ''
for i in nums:
    s += str(i)

s = str(int(s) + 1)

nums = []
for i in s:
    nums.append(i)

print(nums)
