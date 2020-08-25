# Program to create a function to swap numbers


def swap(s1, s2):
    s1, s2 = s2, s1
    print(s1, s2)


x = [1]
y = [2]
swap(x, y)
print(x, y)
