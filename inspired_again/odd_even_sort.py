nums = []
for i in range(int(input())):
    nums.append(int(input()))

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] % 2 == 0 and nums[j] % 2 == 0 and nums[i] > nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        if nums[i] % 2 != 0 and nums[j] % 2 != 0 and nums[i] < nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

print(nums)
