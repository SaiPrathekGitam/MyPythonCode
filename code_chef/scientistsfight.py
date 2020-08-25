nums = ''

for i in range(int(input())):
    for j in range(int(input())):
        nums += input()
    maxi = 1
    for j in nums:
        if nums.count(j) > maxi:
            maxi = nums.count(j)

print(maxi)
