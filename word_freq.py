# Program to calculate word frequency in the given string

s = input("Enter The String : ")
c = s.split(" ")
freq = {}

for i in range(len(c)):
    if c[i] not in freq:
        freq[c[i]] = c.count(c[i])

print(freq)
