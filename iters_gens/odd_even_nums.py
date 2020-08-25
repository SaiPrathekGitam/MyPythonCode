class GenNums:
    def __init__(self, start, end, type='e'):
        self.type = type
        if self.type == 'e':
            if start % 2 == 0:
                self.start = start
            else:
                self.start = start + 1
            self.end = end
        if self.type == 'o':
            if start % 2 == 0:
                self.start = start + 1
            else:
                self.start = start
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


for i in GenNums(1, 10, 'o'):
    print(i)
