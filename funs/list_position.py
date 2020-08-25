# Program to create a function to return position of an element in a list in another list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [4, 7, 1, 6, 2, 9, 8, 3]


def pos(x, y):
    d = {}
    for i in range(len(x)):
        if x[i] in y:
            d[x[i]] = y.index(x[i])
        else:
            d[x[i]] = -1
    return d


print(pos(a, b))
