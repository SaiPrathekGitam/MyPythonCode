nums = []
for i in range(int(input())):
    nums.append(int(input()))

counts = []

for i in range(len(nums)):
    count = 0
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            count += 1
    counts.append(count)

print(counts)
