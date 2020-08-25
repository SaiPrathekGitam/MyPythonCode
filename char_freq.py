# Program to calculate character frequency in the given string

d = {}
s = input("Enter The String : ")

for i in range(len(s)):
    if s[i] not in d:
        d[s[i]] = s.count(s[i])

for i in sorted(d):
    print(i, d[i])
