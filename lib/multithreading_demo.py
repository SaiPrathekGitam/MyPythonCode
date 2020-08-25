# Program to demonstrate mul(tit)hreading

import threading
from threading import Thread


class PrintThread(Thread):
    def run(self):
        for i in range(10):
            print(i)


ct = PrintThread()
ct.start()
print(threading.current_thread())
