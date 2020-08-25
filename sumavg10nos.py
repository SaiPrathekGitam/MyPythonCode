# Program to find sum and average of 10 given numbers
add = avg = 0
for i in range(1, 11):
    n = int(input(f"Enter Number {i} : "))
    add += n

avg = add / 10

print(f"Sum = {add} Average = {avg}")
