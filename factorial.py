def factorial(n):
    fact = 1
    for i in range(1, n):
        fact *= i
    return fact


n = [factorial(n) for n in range(10)]
print(n)
