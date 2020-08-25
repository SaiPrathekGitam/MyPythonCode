# Program to calculate mode, median and mean of given numbers
import statistics
from statistics import StatisticsError

numbers = []

while True:
    n = int(input("Enter The Number (0 to stop) : "))
    if n == 0:
        break
    numbers.append(n)

try:
    print("Mode : ", statistics.mode(numbers))
except StatisticsError:
    print("No Mode Found")

print("Median : ", statistics.median(numbers))
print("Mean : ", statistics.mean(numbers))
