# Program to create a function to reverse given string with case modification


def strrev(a='yay', c='s'):
    a = a[::-1]
    if c == 'u':
        return a.upper()
    elif c == 'l':
        return a.lower()
    else:
        return a


print(strrev(input("Enter The String : ")))
 