def largest(lst):
    lst.sort()
    return lst[len(lst) - 1]


def sec_largest(lst):
    lst.sort()
    return lst[len(lst) - 2]


def odd_even(lst, odd, even):
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)


def sort_double(l1, l2):
    lst = []
    lst = l1 + l2
    lst.sort()
    return lst


def union(l1, l2):
    return list(set(l1) | set(l2))


def intersection(l1, l2):
    return list(set(l1) & set(l2))


def swap_first_last(lst):
    lst[0], lst[len(lst) - 1] = lst[len(lst) - 1], lst[0]
    return lst


def remove_dups(lst):
    return list(set(lst))


def len_of_longest(lst):
    m = len(lst[0])
    for i in lst:
        if len(i) > m:
            m = len(i)
            f = i
    return len(f), f


def list_sum(lst):
    if type(lst[0]) is str:
        total = ""
    elif type(lst[0]) is int:
        total = 0
    for i in lst:
        total += i
    return total
