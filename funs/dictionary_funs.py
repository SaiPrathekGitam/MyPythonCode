# Program to create Dictionary Functions

dic = {1: 'a', 3: 'b', 2: 'c'}
dict = {1: 1, 2: 2, 3: 3}
list1 = [1, 2, 3, 7, 2, 3, 9, 5, 1, 9, 4, 7, 1, 4, 5, 6, 7, 8, 9, 0]
list2 = [11, 22, 33, 44, 66, 88, 77, 1, 4, 7, 90, 6]
list3 = ['saesfasf', 'asfasfeaf', 'afsesf', 'wrgfsffwef', 'werfwefrwefe', 'efrwefrewf', 'ergergfrefaerferger']


def concat(d1, d2):
    d = {}
    for i in d1:
        d[i] = d1[i]
    for i in d2:
        d[i] = d2[i]
    return d


def update(d, key, val):
    d.update({key: val})
    return d


def valid_key(d, key):
    if key in d:
        return True
    else:
        return False


def remove_key(d, key):
    if key in d:
        # print(key, d[key])
        del d[key]
    return d


def lists_to_dic(lst1, lst2):
    d = {}
    for i in range(min(len(lst1), len(lst2))):
        d.update({lst1[i]: lst2[i]})
    return d
