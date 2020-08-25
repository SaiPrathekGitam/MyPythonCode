class EvenNums:
    def __init__(self, start, end):
        if start % 2 == 0:
            self.start = start
        else:
            self.start = start + 1
        self.end = end

    def __iter__(self):
        self.num = self.start
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 2
        return self.num - 2


for i in EvenNums(3, 11):
    print(i)
