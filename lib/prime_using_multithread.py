# Program to print prime numbers using child thread

from threading import Thread
import math


class PrimeThread(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        if self.num == 4:
            print(f"{self.num} is not a prime number")
        else:
            for n in range(2, math.ceil((math.sqrt(self.num)))):
                if self.num % n == 0:
                    print(f"{self.num} is not a prime number")
                    break
            else:
                print(f"{self.num} is a prime number")


# nums = [3453655341, 1212121122111, 29292929292, 349843834853, 6255144141124111]
# for i in nums:
#     t = PrimeThread(i)
#     t.start()

for j in range(1, 26):
    t = PrimeThread(j)
    t.start()
