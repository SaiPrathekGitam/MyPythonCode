# Program to illustrate binary search algorithm

l = [i for i in range(10)]
print(l)

first = 0
last = len(l) - 1

f = int(input('Enter The Number You Want To Find : '))

while f >= 0:
    while first <= last:
        mid = (first + last) // 2
        # print(first, mid, last)
        if l[mid] == f:
            print('Number Found At', mid + 1)
            break
        elif l[mid] > f:
            last = mid - 1
        else:
            first = mid + 1
    else:
        print('Number Not Found')
    first = 0
    last = len(l) - 1
    f = int(input('Enter The Number You Want To Find : '))