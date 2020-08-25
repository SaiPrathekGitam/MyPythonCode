def fun(*nums):
    fac = []
    for i in nums:
        for j in range(1, i + 1):
            if i % j == 0:
                fac.append(j)
    cf = set()
    for i in fac:
        if fac.count(i) == len(nums):
            cf.add(i)
    return cf


print(fun(4, 8, 16, 64))
