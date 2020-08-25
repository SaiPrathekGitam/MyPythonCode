# Program to illustrate iterators and generators
#
# l = [1, 2, 3]
# li = iter(l)
# type(li)
# print(li.__next__())
# print(li.__next__())
# print(li.__next__())
# li.__next__()
#
#
# class Nums_Iterator:
#     def __init__(self):
#         self.num = 1
#
#     def __next__(self):
#         if self.num > 10:
#             raise StopIteration
#         else:
#             self.num += 1
#             return self.num - 1
#
#
# class Nums:
#     def __iter__(self):
#         return Nums_Iterator()
#
#
# n = Nums()
# for i in n:
#     print(i, end=' ')
#
#
# ================================================ Range =================================================
#
#
# class Range_Iterator:
#     def __init__(self, start, end, interval):
#         self.end = end - 1
#         self.interval = interval
#         self.num = start - 1
#
#     def __next__(self):
#         if self.num >= self.end:
#             raise StopIteration
#         else:
#             self.num += self.interval
#             return self.num
#
#
# class Range:
#     def __init__(self, start, end, interval=1):
#         self.start = start
#         self.end = end
#         self.interval = interval
#
#     def __iter__(self):
#         return Range_Iterator(self.start, self.end, self.interval)
#
#
# class Odd_Even_Iterator:
#     def __init__(self, start, end, type):
#         self.type = type
#         self.end = end - 1
#         if (start % 2 == 0 and self.type == 'e') or (start % 2 != 0 and self.type == 'o'):
#             self.num = start
#         else:
#             self.num = start + 1
#
#     def __next__(self):
#         if self.num > self.end:
#             raise StopIteration
#         else:
#             self.num += 2
#             return self.num - 2
#
#
# class Odd_Even:
#     def __init__(self, start, end, type='e'):
#         self.start = start
#         self.end = end
#         self.type = type
#
#     def __iter__(self):
#         return Odd_Even_Iterator(self.start, self.end, self.type)
#
#
# for i in Odd_Even(2, 11, type='e'):
#     print(i, end=' ')

# def nums():
#     for v in range(1, 6):
#         yield v
#
# n = nums()
# print(next(n))


def codes(st):
    for c in st:
        yield ord(c)


for i in codes('Python'):
    print(i)