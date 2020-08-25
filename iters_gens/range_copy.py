class RangeIterator:
    def __init__(self, start, end, interval):
        self.start = start
        self.end = end
        self.interval = interval

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        self.start += self.interval
        return self.start - self.interval


class Range:
    def __init__(self, start, end, interval=1):
        self.start = start
        self.end = end
        self.interval = interval

    def __iter__(self):
        return RangeIterator(self.start, self.end, self.interval)


r = Range(1, 11)
for i in r:
    print(i, end=' ')
