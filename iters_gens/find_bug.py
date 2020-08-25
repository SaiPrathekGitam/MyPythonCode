class Marks:
    def __init__(self):
        self.marks = [10, 20, 30, 40]

    def __iter__(self):  # defining iterator method
        self.pos = 0  # start at zero to iterate again
        return self

    def __next__(self):
        if self.pos == len(self.marks):
            raise StopIteration
        else:
            self.pos += 1
            return self.marks[self.pos - 1]


m = Marks()
mi = iter(m)

M = Marks()
Mi = iter(M)

print(m.__next__())
print(M.__next__())
print(next(m))
print(next(M))
