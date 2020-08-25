# Program to use multithreading to write whether number is prime or not into a file

import threading
from threading import Thread

f = open("prime.txt", "wt")


class PrimeThread(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        for n in range(2, self.num // 2):
            if self.num % n == 0:
                f.write(f"\n{self.num} is not a prime number")
                break
        else:
            f.write(f"\n{self.num} is a prime number")


for n in range(1, 101):
    t = PrimeThread(n)
    t.start()

for i in threading.enumerate():
    if i != threading.current_thread():
        threading.join()

f.close()
