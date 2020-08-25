nums = []

for i in range(int(input())):
    nums.append(int(input()))

counts = []

for i in nums:
    counts.append(nums.count(i))

print(max(counts))
