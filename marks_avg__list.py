# Program to print marks greater than the average marks
import statistics

marks = []

for i in range(10):
    n = int(input("Enter The Marks : "))
    marks.append(n)

avg = statistics.mean(marks)

print(f"Marks Greater than Average ({avg})are")

for i in range(10):
    if marks[i] > avg:
        print(marks[i])
